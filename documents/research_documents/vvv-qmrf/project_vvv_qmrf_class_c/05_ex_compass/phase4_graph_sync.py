"""
Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

VVV-QMRF-EX Phase 4 Graph Sync (A.1+ helper for plan v1.6 design gap F-RCA-12)

Purpose:
  After phase1 re-creates graph.json from SOT, only 149 edges exist
  (115 VVV + 13 BR + 21 draft). Phase 4 originally added 11 new BR_EX_*
  edges (BR_EX_BE_00037 sim candidate + 9 KE-PM Phase 6 + 1 BR_EX_QM
  sim candidate). Phase 7 added 23 more BR_EX_BE stretch entries.
  Phase 8 then audited 143 registry entries (69 BE + 74 QM).

  Phase1 re-run loses all 34 NEW entries (non-reference_copy). This
  script reads both registries and re-injects the missing edges so
  Phase 2 intersection analysis sees the complete v1.6 state.

  Reference_copy entries (36 BE + 73 QM = 109) are already represented
  in the graph via existing edge types (DRAFT_BRIDGE_BE_VVV, VVV_TO_BE,
  VVV_TO_QM, BR_QM_VVV) — they require no injection.

Idempotent: safe to re-run; skips edges already present by br_ex_id.
"""

import os
import re
import sys
import json
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE = Path(os.path.dirname(os.path.abspath(__file__)))
DATA = BASE / "data"
BE_REGISTRY_MD = BASE / "br_ex_be_registry.md"
QM_REGISTRY_MD = BASE / "br_ex_qm_registry.md"
GRAPH_JSON = DATA / "vvv_qmrf_ex_graph.json"

EDGE_TYPE_BY_KIND = {
    "BE": {
        "new_similarity_candidate": "BR_EX_BE",
        "expert_manual_mapping": "BR_EX_BE_NEW",
        "stretch_expert_mapping": "BR_EX_BE_STRETCH",
    },
    "QM": {
        "new_similarity_candidate": "BR_EX_QM",
    },
}


def parse_registry(md_path, kind):
    text = md_path.read_text(encoding="utf-8")
    entries = []
    pattern = r"###\s+(BR_EX_[A-Z]+_\d+)([\s\S]*?)(?=^###\s+BR_EX_|\Z)"
    for m in re.finditer(pattern, text, re.MULTILINE):
        eid = m.group(1)
        section = m.group(2)
        type_m = re.search(r"\*\*Type\*\*\s*\|\s*([^|\n]+)", section)
        etype = type_m.group(1).strip() if type_m else "unknown"
        if etype == "reference_copy":
            continue
        # v1.7: skip reclassified entries (no longer active in current graph)
        if "RECLASSIFIED" in etype:
            print(f"[SKIP-v1.7] {eid} — type={etype}")
            continue
        if kind == "BE":
            src = re.search(r"\*\*BE Node\*\*\s*\|\s*`(N_BE_\d+)`", section)
            tgt = re.search(r"\*\*VVV Node\*\*\s*\|\s*`(N_QM_VVV_\d+)`", section)
        else:
            src = re.search(r"\*\*VVV Node\*\*\s*\|\s*`(N_QM_VVV_\d+)`", section)
            tgt = re.search(r"\*\*QM Node\*\*\s*\|\s*`(N_QM_\d+)`", section)
        rel = re.search(r"\*\*Relation Type\*\*\s*\|\s*([^|\n]+)", section)
        claim = re.search(r"\*\*Claim Class\*\*\s*\|\s*([^|\n]+)", section)
        conf = re.search(r"\*\*Confidence\*\*\s*\|\s*([0-9.]+)", section)
        if not (src and tgt):
            print(f"[WARN] {eid} missing node fields — skipped")
            continue
        edge_type = EDGE_TYPE_BY_KIND[kind].get(etype, f"BR_EX_{kind}")
        entries.append({
            "br_ex_id": eid,
            "registry_type": etype,
            "source": src.group(1),
            "target": tgt.group(1),
            "edge_type": edge_type,
            "relation": rel.group(1).strip() if rel else "unspecified",
            "claim_class": claim.group(1).strip() if claim else "interpretive_mapping",
            "confidence": float(conf.group(1)) if conf else 0.0,
        })
    return entries


def main():
    be_entries = parse_registry(BE_REGISTRY_MD, "BE")
    qm_entries = parse_registry(QM_REGISTRY_MD, "QM")
    print(f"[OK] Parsed BE registry: {len(be_entries)} non-reference_copy entries")
    print(f"[OK] Parsed QM registry: {len(qm_entries)} non-reference_copy entries")
    print(f"[OK] Total to inject: {len(be_entries) + len(qm_entries)}")

    with open(GRAPH_JSON, "r", encoding="utf-8") as f:
        g = json.load(f)
    # NetworkX json_graph uses "links" (3.x default) or "edges" (custom). Detect.
    if "links" in g and g["links"]:
        edge_key = "links"
    elif "edges" in g and g["edges"]:
        edge_key = "edges"
    elif "links" in g:
        edge_key = "links"
    else:
        edge_key = "edges"
    edges = g.setdefault(edge_key, [])
    edges_before = len(edges)
    print(f"[INFO] Graph before sync: {edges_before} edges (key='{edge_key}')")

    existing_ids = {e.get("br_ex_id") for e in edges if e.get("br_ex_id")}

    injected = {"BE": 0, "QM": 0}
    skipped = {"BE": 0, "QM": 0}

    for kind, entry_list in [("BE", be_entries), ("QM", qm_entries)]:
        for entry in entry_list:
            if entry["br_ex_id"] in existing_ids:
                skipped[kind] += 1
                continue
            phase_label = {
                "BR_EX_BE": "phase4-sim",
                "BR_EX_BE_NEW": "phase6-expert",
                "BR_EX_BE_STRETCH": "phase7-stretch",
                "BR_EX_QM": "phase4-sim",
            }.get(entry["edge_type"], "phase4-sync")
            edges.append({
                "source": entry["source"],
                "target": entry["target"],
                "edge_type": entry["edge_type"],
                "relation": entry["relation"],
                "claim_class": entry["claim_class"],
                "br_ex_id": entry["br_ex_id"],
                "similarity": entry["confidence"],
                "phase": phase_label,
            })
            injected[kind] += 1

    edges_after = len(edges)
    print(f"[OK] Injected BE: {injected['BE']}; QM: {injected['QM']}")
    print(f"[OK] Skipped already-present: BE={skipped['BE']}, QM={skipped['QM']}")
    print(f"[OK] Graph after sync: {edges_after} edges (delta +{edges_after - edges_before})")

    with open(GRAPH_JSON, "w", encoding="utf-8") as f:
        json.dump(g, f, ensure_ascii=False, indent=2)
    print(f"[OK] Saved: {GRAPH_JSON}")

    context_path = DATA / "vvv_qmrf_ex_context.json"
    if context_path.exists():
        with open(context_path, "r", encoding="utf-8") as f:
            ctx = json.load(f)
        if "edge_count" in ctx:
            old = ctx["edge_count"]
            ctx["edge_count"] = edges_after
            print(f"[OK] context.json edge_count: {old} -> {edges_after}")
        for _, v in ctx.items():
            if isinstance(v, dict) and "edge_count" in v:
                v["edge_count"] = edges_after
        ctx["graph_sync_v1_6"] = {
            "applied": True,
            "injected_be": injected["BE"],
            "injected_qm": injected["QM"],
            "skipped_be": skipped["BE"],
            "skipped_qm": skipped["QM"],
            "edges_before": edges_before,
            "edges_after": edges_after,
        }
        with open(context_path, "w", encoding="utf-8") as f:
            json.dump(ctx, f, ensure_ascii=False, indent=2)
        print(f"[OK] Saved: {context_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
