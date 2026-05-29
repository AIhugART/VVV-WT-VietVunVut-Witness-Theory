"""
VVV-QMRF-EX Phase 3 — Similarity Search
Plan: vvv-qmrf-ex-plan.md §7 Phase 3 (Steps 3.1-3.6)
Execution: C:/Users/PC/AppData/Local/Programs/Python/Python312/python.exe

Steps:
  3.1 Generate embeddings for all 420 nodes (all-mpnet-base-v2, dim=768)
      Record model + version + dim into vvv_qmrf_ex_context.json (F4 RCA)
  3.2 Compute 263x52 BE<->VVV cosine similarity matrix
  3.3 Compute 52x105 VVV<->QM cosine similarity matrix
  3.4 Apply thresholds: >=0.75 Tier1, 0.50-0.74 Tier2, 0.30-0.49 manual
  3.5 Cross-reference candidates against existing graph edges (filter known)
  3.6 Report top candidates per VVV node (especially K-gap nodes from Phase 2)

Outputs (all in vvv-qmrf-ex/data/):
  vvv_qmrf_ex_similarity_be_vvv.csv   (263x52 matrix, rows=BE, cols=VVV)
  vvv_qmrf_ex_similarity_vvv_qm.csv   (52x105 matrix, rows=VVV, cols=QM)
  vvv_qmrf_ex_context.json            (project context snapshot + model metadata)
  phase3_similarity_report.json       (tier-classified candidates + gap analysis)

Embedding text strategy:
  Use full 'concept' field for all nodes.
  VVV concepts are already long and descriptive.
  BE and QM concepts are short -- layer appended for additional context.
"""

import csv
import json
import os
import sys
from pathlib import Path

import numpy as np

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SUFFIX = os.environ.get("VVV_QMRF_EX_SUFFIX", "")

# ── Paths ─────────────────────────────────────────────────────────────────────
BASE = Path("c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement")
OUT  = BASE / "documents/research_documents/vvv-qmrf-ex"
DATA = OUT / "data"

GRAPH_JSON  = DATA / "vvv_qmrf_ex_graph.json"
PHASE2_JSON = DATA / f"phase2_intersection_report{SUFFIX}.json"

MODEL_NAME = "sentence-transformers/all-mpnet-base-v2"
EMB_DIM    = 768

TIER1_MIN  = 0.75
TIER2_MIN  = 0.50
MANUAL_MIN = 0.30

K_SIDE_TYPES   = {"VVV_TO_BE", "DRAFT_BRIDGE_BE_VVV"}
RHO_SIDE_TYPES = {"VVV_TO_QM", "BR_QM_VVV"}


# ── Load graph ────────────────────────────────────────────────────────────────
def load_graph_json(path: Path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def extract_nodes_by_system(data, system: str):
    nodes = []
    for n in data["nodes"]:
        if n.get("system") == system:
            nodes.append((n["id"], n.get("concept", ""), n.get("layer", "")))
    return sorted(nodes, key=lambda x: x[0])


def build_existing_pairs(data):
    sys_map = {n["id"]: n.get("system") for n in data["nodes"]}
    existing_be_vvv = set()
    existing_vvv_qm = set()

    # NetworkX 3.x node_link_data uses key "edges" (not "links")
    for link in data.get("edges", data.get("links", [])):
        src = link.get("source")
        tgt = link.get("target")
        et  = link.get("edge_type", "")

        if et in K_SIDE_TYPES:
            s_sys, t_sys = sys_map.get(src), sys_map.get(tgt)
            if s_sys == "BE"  and t_sys == "VVV": existing_be_vvv.add((src, tgt))
            if s_sys == "VVV" and t_sys == "BE":  existing_be_vvv.add((tgt, src))

        if et in RHO_SIDE_TYPES:
            s_sys, t_sys = sys_map.get(src), sys_map.get(tgt)
            if s_sys == "VVV" and t_sys == "QM": existing_vvv_qm.add((src, tgt))
            if s_sys == "QM"  and t_sys == "VVV": existing_vvv_qm.add((tgt, src))

    return existing_be_vvv, existing_vvv_qm


# ── Embedding text construction ───────────────────────────────────────────────
def make_text(node_id: str, concept: str, layer: str, system: str) -> str:
    concept = concept.strip()
    layer   = layer.strip()
    if system == "VVV":
        return concept
    if layer and layer.lower() not in ("", "rca", "?"):
        return f"{concept} ({layer})"
    return concept


# ── 3.1  Generate embeddings ──────────────────────────────────────────────────
def generate_embeddings(texts: list, model_name: str):
    from sentence_transformers import SentenceTransformer
    print(f"  Loading model: {model_name}")
    model = SentenceTransformer(model_name)
    actual_dim = model.get_sentence_embedding_dimension()
    print(f"  Model dim: {actual_dim}  (expected {EMB_DIM})")
    print(f"  Encoding {len(texts)} texts (batch_size=64)...")
    embeddings = model.encode(
        texts,
        batch_size=64,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=True,
    )
    return embeddings, actual_dim


# ── 3.2/3.3  Cosine similarity ────────────────────────────────────────────────
def cosine_sim_matrix(emb_a: np.ndarray, emb_b: np.ndarray) -> np.ndarray:
    # Both L2-normalized -> cosine = dot product
    return emb_a @ emb_b.T


# ── 3.4  Threshold classification ────────────────────────────────────────────
def classify_tier(score: float) -> str:
    if score >= TIER1_MIN:  return "tier1"
    if score >= TIER2_MIN:  return "tier2"
    if score >= MANUAL_MIN: return "manual"
    return "excluded"


# ── 3.5  Build candidate list ────────────────────────────────────────────────
def build_candidates(sim_matrix, row_nodes, col_nodes, existing_pairs, top_per_row=5):
    all_new = []
    per_row_top = {}

    for i, (rid, rconcept, _) in enumerate(row_nodes):
        row_scored = []
        for j, (cid, cconcept, _) in enumerate(col_nodes):
            score = float(sim_matrix[i, j])
            tier  = classify_tier(score)
            if tier == "excluded":
                continue
            is_new = (rid, cid) not in existing_pairs
            entry = {
                "row_node": rid, "row_concept": rconcept[:60],
                "col_node": cid, "col_concept": cconcept[:60],
                "score": round(score, 6), "tier": tier, "is_new": is_new,
            }
            if is_new:
                all_new.append(entry)
            row_scored.append(entry)

        row_scored.sort(key=lambda x: x["score"], reverse=True)
        per_row_top[rid] = row_scored[:top_per_row]

    all_new.sort(key=lambda x: x["score"], reverse=True)
    return all_new, per_row_top


# ── Save CSV matrix ───────────────────────────────────────────────────────────
def save_similarity_csv(path: Path, sim_matrix, row_nodes, col_nodes, decimals=4):
    fmt = f".{decimals}f"
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["node_id"] + [n[0] for n in col_nodes])
        for i, (rid, _, _) in enumerate(row_nodes):
            writer.writerow(
                [rid] + [format(float(sim_matrix[i, j]), fmt) for j in range(len(col_nodes))]
            )
    print(f"  Saved: {path}  ({len(row_nodes)} rows x {len(col_nodes)} cols)")


# ── Main ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 60)
    print("VVV-QMRF-EX  Phase 3 -- Similarity Search")
    print("=" * 60)

    graph_data = load_graph_json(GRAPH_JSON)
    be_nodes   = extract_nodes_by_system(graph_data, "BE")
    vvv_nodes  = extract_nodes_by_system(graph_data, "VVV")
    qm_nodes   = extract_nodes_by_system(graph_data, "QM")

    with open(PHASE2_JSON, encoding="utf-8") as f:
        phase2 = json.load(f)
    k_gap_ids   = set(phase2["k_gaps"].keys())
    rho_gap_ids = set(phase2["rho_gaps"].keys())

    print(f"\nNodes: {len(be_nodes)} BE, {len(vvv_nodes)} VVV, {len(qm_nodes)} QM")
    print(f"K-gap VVV (Phase 2): {len(k_gap_ids)}  |  rho-gap: {len(rho_gap_ids)}")

    existing_be_vvv, existing_vvv_qm = build_existing_pairs(graph_data)
    print(f"Existing BE-VVV pairs: {len(existing_be_vvv)}  |  VVV-QM: {len(existing_vvv_qm)}")

    # 3.1 Embeddings
    print("\nStep 3.1  Generating embeddings...")
    be_texts  = [make_text(*n, "BE")  for n in be_nodes]
    vvv_texts = [make_text(*n, "VVV") for n in vvv_nodes]
    qm_texts  = [make_text(*n, "QM")  for n in qm_nodes]

    embeddings, actual_dim = generate_embeddings(be_texts + vvv_texts + qm_texts, MODEL_NAME)

    n_be, n_vvv, n_qm = len(be_nodes), len(vvv_nodes), len(qm_nodes)
    emb_be  = embeddings[:n_be]
    emb_vvv = embeddings[n_be:n_be + n_vvv]
    emb_qm  = embeddings[n_be + n_vvv:]

    assert emb_be.shape  == (n_be,  actual_dim)
    assert emb_vvv.shape == (n_vvv, actual_dim)
    assert emb_qm.shape  == (n_qm,  actual_dim)
    print(f"  [OK] Shapes: BE={emb_be.shape}, VVV={emb_vvv.shape}, QM={emb_qm.shape}")

    # 3.2 BE <-> VVV
    print("\nStep 3.2  BE<->VVV similarity matrix...")
    sim_be_vvv = cosine_sim_matrix(emb_be, emb_vvv)
    assert sim_be_vvv.shape == (n_be, n_vvv)
    print(f"  Shape: {sim_be_vvv.shape}  min={sim_be_vvv.min():.4f}  max={sim_be_vvv.max():.4f}")
    print(f"  [OK] Shape = ({n_be}, {n_vvv})")

    # 3.3 VVV <-> QM
    print("\nStep 3.3  VVV<->QM similarity matrix...")
    sim_vvv_qm = cosine_sim_matrix(emb_vvv, emb_qm)
    assert sim_vvv_qm.shape == (n_vvv, n_qm)
    print(f"  Shape: {sim_vvv_qm.shape}  min={sim_vvv_qm.min():.4f}  max={sim_vvv_qm.max():.4f}")
    print(f"  [OK] Shape = ({n_vvv}, {n_qm})")

    # 3.4 / 3.5
    print("\nStep 3.4/3.5  Threshold + cross-reference...")
    be_vvv_cands, be_vvv_top = build_candidates(sim_be_vvv, be_nodes, vvv_nodes, existing_be_vvv)
    vvv_qm_cands, vvv_qm_top = build_candidates(sim_vvv_qm, vvv_nodes, qm_nodes, existing_vvv_qm)

    be_vvv_t1 = [c for c in be_vvv_cands if c["tier"] == "tier1"]
    be_vvv_t2 = [c for c in be_vvv_cands if c["tier"] == "tier2"]
    vvv_qm_t1 = [c for c in vvv_qm_cands if c["tier"] == "tier1"]
    vvv_qm_t2 = [c for c in vvv_qm_cands if c["tier"] == "tier2"]

    print(f"  BE->VVV new: Tier1={len(be_vvv_t1)}  Tier2={len(be_vvv_t2)}")
    print(f"  VVV->QM new: Tier1={len(vvv_qm_t1)}  Tier2={len(vvv_qm_t2)}")

    # 3.6 Gap-focused top matches
    print("\nStep 3.6  K-gap VVV nodes — best BE matches:")
    vvv_ids = [n[0] for n in vvv_nodes]
    k_gap_be_top = {}
    for vvv_id in sorted(k_gap_ids):
        if vvv_id not in vvv_ids:
            continue
        vi = vvv_ids.index(vvv_id)
        top5 = sorted(
            [(float(sim_be_vvv[bi, vi]), be_nodes[bi][0], be_nodes[bi][1]) for bi in range(n_be)],
            key=lambda x: x[0], reverse=True
        )[:5]
        k_gap_be_top[vvv_id] = [
            {"be_node": n, "be_concept": c[:60], "score": round(s, 6), "tier": classify_tier(s)}
            for s, n, c in top5
        ]
        best = k_gap_be_top[vvv_id][0]
        print(f"  {vvv_id}:  best={best['be_node']} ({best['be_concept'][:38]}) {best['score']:.4f} [{best['tier']}]")

    # Save outputs
    print("\nSaving outputs...")
    save_similarity_csv(DATA / "vvv_qmrf_ex_similarity_be_vvv.csv", sim_be_vvv, be_nodes, vvv_nodes)
    save_similarity_csv(DATA / "vvv_qmrf_ex_similarity_vvv_qm.csv", sim_vvv_qm, vvv_nodes, qm_nodes)

    context = {
        "project_name":       "VVV-QMRF-EX",
        "version":            "0.3-phase3",
        "date":               "2026-05-20",
        "phases_complete":    ["0-environment", "1-graph-construction",
                               "2-intersection-analysis", "3-similarity-search"],
        "graph": {
            "total_nodes": n_be + n_vvv + n_qm,
            "be_count": n_be, "vvv_count": n_vvv, "qm_count": n_qm,
            "edge_count": len(graph_data.get("links", [])),
        },
        "embedding_model":    MODEL_NAME,
        "embedding_dim":      actual_dim,
        "embedding_normalize": True,
        "similarity_metric":  "cosine (dot product of L2-normalized vectors)",
        "matrix_shapes":      {"be_vvv": [n_be, n_vvv], "vvv_qm": [n_vvv, n_qm]},
        "thresholds":         {"tier1": TIER1_MIN, "tier2_min": TIER2_MIN, "manual_min": MANUAL_MIN},
        "phase2_summary": {
            "intersection_count": phase2["intersection_count"],
            "k_gap_count": len(k_gap_ids),
            "rho_gap_count": len(rho_gap_ids),
        },
        "phase3_summary": {
            "be_vvv_new_tier1": len(be_vvv_t1),
            "be_vvv_new_tier2": len(be_vvv_t2),
            "vvv_qm_new_tier1": len(vvv_qm_t1),
            "vvv_qm_new_tier2": len(vvv_qm_t2),
        },
    }
    context_path = DATA / "vvv_qmrf_ex_context.json"
    with open(context_path, "w", encoding="utf-8") as f:
        json.dump(context, f, indent=2, ensure_ascii=False)
    print(f"  Saved context: {context_path}")

    report = {
        "phase": "3-similarity-search",
        "date": "2026-05-20",
        "model": MODEL_NAME,
        "embedding_dim": actual_dim,
        "matrix_shapes": {"be_vvv": [n_be, n_vvv], "vvv_qm": [n_vvv, n_qm]},
        "thresholds": {"tier1": TIER1_MIN, "tier2_min": TIER2_MIN, "manual_min": MANUAL_MIN},
        "be_vvv_stats": {
            "total_new": len(be_vvv_cands),
            "tier1": len(be_vvv_t1),
            "tier2": len(be_vvv_t2),
            "manual": len([c for c in be_vvv_cands if c["tier"] == "manual"]),
        },
        "vvv_qm_stats": {
            "total_new": len(vvv_qm_cands),
            "tier1": len(vvv_qm_t1),
            "tier2": len(vvv_qm_t2),
            "manual": len([c for c in vvv_qm_cands if c["tier"] == "manual"]),
        },
        "be_vvv_tier1_candidates": be_vvv_t1[:60],
        "be_vvv_tier2_candidates": be_vvv_t2[:60],
        "vvv_qm_tier1_candidates": vvv_qm_t1[:60],
        "vvv_qm_tier2_candidates": vvv_qm_t2[:60],
        "be_vvv_top_per_vvv_node": be_vvv_top,
        "vvv_qm_top_per_vvv_node": vvv_qm_top,
        "k_gap_be_top_matches": k_gap_be_top,
        "integrity_checks": {
            "matrix_be_vvv_shape": list(sim_be_vvv.shape) == [n_be, n_vvv],
            "matrix_vvv_qm_shape": list(sim_vvv_qm.shape) == [n_vvv, n_qm],
            "model_recorded":      True,
            "dim_recorded":        True,
        },
    }
    report_path = DATA / f"phase3_similarity_report{SUFFIX}.json"
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"  Saved report:  {report_path}")

    all_pass = all(report["integrity_checks"].values())
    print("\n" + "=" * 60)
    print("Phase 3 complete.")
    print(f"  Embeddings:     {n_be + n_vvv + n_qm} nodes @ dim={actual_dim}")
    print(f"  BE<->VVV:       {sim_be_vvv.shape}  max={sim_be_vvv.max():.4f}")
    print(f"  VVV<->QM:       {sim_vvv_qm.shape}  max={sim_vvv_qm.max():.4f}")
    print(f"  BE->VVV new:    Tier1={len(be_vvv_t1)}  Tier2={len(be_vvv_t2)}")
    print(f"  VVV->QM new:    Tier1={len(vvv_qm_t1)}  Tier2={len(vvv_qm_t2)}")
    print(f"  Integrity:      {'[OK] All checks pass' if all_pass else '[FAIL]'}")
    print("=" * 60)
