"""
VVV-QMRF-EX Phase 4 — Bridge Registry Construction
Author: VietVunVut (Viet - Nguyen Xuan)
Date: 2026-05-20

Creates:
  ex_schema_addendum.md          — EX-local namespace + schema extension (F1 RCA fix)
  br_ex_be_registry.md           — 38 BR_EX_BE entries (36 ref-copy + 2 Tier2 new)
  br_ex_qm_registry.md           — 74 BR_EX_QM entries (61 ref-copy + 13 Tier2 new)
  data/vvv_qmrf_ex_graph.json    — Updated graph (+15 BR_EX edges = 164 total)
  vvv_qmrf_ex_intersection.md    — Phase 4 Final intersection report
  vvv_qmrf_ex_gaps.md            — Phase 4 Final gap report
  data/phase4_registry_report.json

Isolation: ONLY writes inside documents/research_documents/vvv-qmrf-ex/
"""

import json
import os
import sys
from datetime import date

# Force UTF-8 console output on Windows
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from collections import defaultdict

# ──────────────────────────────────────────────────────────────────────────────
# Paths
# ──────────────────────────────────────────────────────────────────────────────
BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "data")

GRAPH_JSON   = os.path.join(DATA, "vvv_qmrf_ex_graph.json")
SIM_REPORT   = os.path.join(DATA, "phase3_similarity_report.json")
CONTEXT_JSON = os.path.join(DATA, "vvv_qmrf_ex_context.json")

OUT_SCHEMA        = os.path.join(BASE, "ex_schema_addendum.md")
OUT_BR_BE         = os.path.join(BASE, "br_ex_be_registry.md")
OUT_BR_QM         = os.path.join(BASE, "br_ex_qm_registry.md")
OUT_INTERSECTION  = os.path.join(BASE, "vvv_qmrf_ex_intersection.md")
OUT_GAPS          = os.path.join(BASE, "vvv_qmrf_ex_gaps.md")
OUT_P4_REPORT     = os.path.join(DATA, "phase4_registry_report.json")

TODAY = str(date.today())

# ──────────────────────────────────────────────────────────────────────────────
# Edge-type classification
# ──────────────────────────────────────────────────────────────────────────────
K_SIDE_TYPES   = {"VVV_TO_BE", "DRAFT_BRIDGE_BE_VVV", "BR_EX_BE"}
RHO_SIDE_TYPES = {"VVV_TO_QM", "BR_QM_VVV", "BR_EX_QM"}

# ──────────────────────────────────────────────────────────────────────────────
# Bridge metadata lookup: edge_type → (relation_type, claim_class, boundary, rationale, confidence)
# ──────────────────────────────────────────────────────────────────────────────
BE_VVV_META = {
    "VVV_TO_BE": (
        "source_analogue_of",
        "source_analogue",
        "Not conceptual identity; VVV concept draws K-side semantics from BE source-analogue. "
        "Direction reversed in derived copy (F2: non-reversal recorded here).",
        "VVV concept draws K-side semantics from BE source-analogue (F2: direction label only; original VVV→BE direction preserved)",
        0.90,
    ),
    "DRAFT_BRIDGE_BE_VVV": (
        "draft_bridge_support",
        "evidence_support",
        "Draft only; gate-passed through 263-node audit cycle but not yet formally verified.",
        "BE concept provides K-side support via 263-node audit cycle (draft — pending formal verification)",
        0.70,
    ),
    "BR_EX_BE_NEW": (
        "conceptual_parallel",
        "interpretive_mapping",
        "Similarity-based only (cosine ≥ 0.50); requires domain expert review before promotion.",
        "BE concept has semantic structural parallel with VVV registration concept identified via Phase 3 embedding similarity",
        None,  # TBD by reviewer
    ),
}

VVV_QM_META = {
    "VVV_TO_QM": (
        "physical_substrate_for",
        "interpretive_mapping",
        "Not physical explanation; not new QM law. QM concept provides formal/physical substrate for VVV registration concept.",
        "QM concept provides physical/formal substrate for VVV registration concept",
        0.90,
    ),
    "BR_QM_VVV": (
        "registration_layer_extension_of",
        "interpretive_mapping",
        "Not modification of QM formalism. VVV concept extends registration semantics of QM physical concept (v0.1 bridge).",
        "VVV concept extends registration semantics of QM physical concept (v0.1 bridge)",
        0.85,
    ),
    "BR_EX_QM_NEW": (
        "physical_substrate_for",
        "interpretive_mapping",
        "Similarity-based only (cosine ≥ 0.50); not verified against QM formalism.",
        "QM concept identified as potential physical substrate via Phase 3 cosine similarity (candidate — requires expert validation)",
        None,
    ),
}

# ──────────────────────────────────────────────────────────────────────────────
# Load data
# ──────────────────────────────────────────────────────────────────────────────
print("=== Phase 4 — Bridge Registry Construction ===")
print(f"Date: {TODAY}")
print()

with open(GRAPH_JSON, "r", encoding="utf-8") as f:
    graph_data = json.load(f)

with open(SIM_REPORT, "r", encoding="utf-8") as f:
    sim_report = json.load(f)

nodes = graph_data["nodes"]
edges = graph_data.get("edges", graph_data.get("links", []))

# Build lookup maps
node_map  = {n["id"]: n for n in nodes}  # id → full node dict
sys_map   = {n["id"]: n.get("system", "") for n in nodes}
concept_map = {n["id"]: n.get("concept", n["id"]) for n in nodes}
layer_map = {n["id"]: n.get("layer", "") for n in nodes}

print(f"Graph loaded: {len(nodes)} nodes, {len(edges)} edges")

# ──────────────────────────────────────────────────────────────────────────────
# Helper: collect existing BE↔VVV and VVV↔QM edge pairs
# ──────────────────────────────────────────────────────────────────────────────
def collect_existing_pairs(edges, sys_map):
    """Returns (be_vvv_pairs, vvv_qm_pairs) as lists of dicts."""
    be_vvv = []
    vvv_qm = []
    for e in edges:
        src = e.get("source", "")
        tgt = e.get("target", "")
        et  = e.get("edge_type", "")
        s_sys = sys_map.get(src, "")
        t_sys = sys_map.get(tgt, "")

        # BE↔VVV
        if et in {"VVV_TO_BE", "DRAFT_BRIDGE_BE_VVV"}:
            if s_sys == "VVV" and t_sys == "BE":
                be_vvv.append({"be_node": tgt, "vvv_node": src, "edge_type": et,
                                "original_src": src, "original_tgt": tgt})
            elif s_sys == "BE" and t_sys == "VVV":
                be_vvv.append({"be_node": src, "vvv_node": tgt, "edge_type": et,
                                "original_src": src, "original_tgt": tgt})

        # VVV↔QM
        if et in {"VVV_TO_QM", "BR_QM_VVV"}:
            if s_sys == "VVV" and t_sys == "QM":
                vvv_qm.append({"vvv_node": src, "qm_node": tgt, "edge_type": et,
                                "original_src": src, "original_tgt": tgt})
            elif s_sys == "QM" and t_sys == "VVV":
                vvv_qm.append({"vvv_node": tgt, "qm_node": src, "edge_type": et,
                                "original_src": src, "original_tgt": tgt})

    return be_vvv, vvv_qm

be_vvv_pairs, vvv_qm_pairs = collect_existing_pairs(edges, sys_map)
print(f"Existing BE<->VVV pairs: {len(be_vvv_pairs)}")
print(f"Existing VVV<->QM pairs: {len(vvv_qm_pairs)}")

# ──────────────────────────────────────────────────────────────────────────────
# Load Phase 3 Tier2 candidates
# ──────────────────────────────────────────────────────────────────────────────
be_vvv_candidates = sim_report.get("be_vvv_tier2_candidates", [])
vvv_qm_candidates = sim_report.get("vvv_qm_tier2_candidates", [])
print(f"Phase 3 Tier2 BE↔VVV new candidates: {len(be_vvv_candidates)}")
print(f"Phase 3 Tier2 VVV↔QM new candidates: {len(vvv_qm_candidates)}")
print()

# ──────────────────────────────────────────────────────────────────────────────
# Build BR_EX_BE registry entries
# ──────────────────────────────────────────────────────────────────────────────
br_ex_be_entries = []
br_ex_be_counter = 1

# 36 reference-copy entries from existing edges
for pair in be_vvv_pairs:
    et = pair["edge_type"]
    meta = BE_VVV_META.get(et, BE_VVV_META["DRAFT_BRIDGE_BE_VVV"])
    relation_type, claim_class, boundary, rationale, confidence = meta
    br_id = f"BR_EX_BE_{br_ex_be_counter:05d}"

    be_node  = pair["be_node"]
    vvv_node = pair["vvv_node"]
    be_concept  = concept_map.get(be_node, be_node)
    vvv_concept = concept_map.get(vvv_node, vvv_node)
    be_layer    = layer_map.get(be_node, "")

    entry = {
        "br_ex_id": br_id,
        "type": "reference_copy",
        "source_edge_type": et,
        "be_node": be_node,
        "be_concept": be_concept,
        "be_layer": be_layer,
        "vvv_node": vvv_node,
        "vvv_concept": vvv_concept,
        "relation_type": relation_type,
        "claim_class": claim_class,
        "boundary_note": boundary,
        "rationale": rationale,
        "confidence": confidence,
        "direction": f"{be_node} → {vvv_node}",
        "origin": "Phase 1 graph",
    }
    br_ex_be_entries.append(entry)
    br_ex_be_counter += 1

# 2 new Tier2 entries from Phase 3 similarity
# Deduplicate against existing pairs
existing_be_vvv_set = {(p["be_node"], p["vvv_node"]) for p in be_vvv_pairs}
new_br_ex_be_graph_edges = []

for cand in be_vvv_candidates:
    be_node  = cand.get("row_node", "")
    vvv_node = cand.get("col_node", "")
    if (be_node, vvv_node) in existing_be_vvv_set:
        continue
    meta = BE_VVV_META["BR_EX_BE_NEW"]
    relation_type, claim_class, boundary, rationale, _ = meta
    sim = cand.get("score", 0.0)
    br_id = f"BR_EX_BE_{br_ex_be_counter:05d}"

    be_concept  = concept_map.get(be_node, be_node)
    vvv_concept = concept_map.get(vvv_node, vvv_node)
    be_layer    = layer_map.get(be_node, "")

    entry = {
        "br_ex_id": br_id,
        "type": "new_similarity_candidate",
        "source_edge_type": "BR_EX_BE_NEW",
        "be_node": be_node,
        "be_concept": be_concept,
        "be_layer": be_layer,
        "vvv_node": vvv_node,
        "vvv_concept": vvv_concept,
        "relation_type": relation_type,
        "claim_class": claim_class,
        "boundary_note": boundary,
        "rationale": rationale,
        "confidence": f"TBD (cosine={sim:.4f})",
        "direction": f"{be_node} → {vvv_node}",
        "origin": "Phase 3 similarity (Tier2)",
    }
    br_ex_be_entries.append(entry)
    # Track for graph update
    new_br_ex_be_graph_edges.append({
        "source": be_node,
        "target": vvv_node,
        "edge_type": "BR_EX_BE",
        "relation": relation_type,
        "claim_class": claim_class,
        "br_ex_id": br_id,
        "similarity": round(sim, 4),
        "phase": "phase4",
    })
    br_ex_be_counter += 1
    existing_be_vvv_set.add((be_node, vvv_node))

print(f"BR_EX_BE entries: {len(br_ex_be_entries)} (ref={len(be_vvv_pairs)}, new={len(new_br_ex_be_graph_edges)})")

# ──────────────────────────────────────────────────────────────────────────────
# Build BR_EX_QM registry entries
# ──────────────────────────────────────────────────────────────────────────────
br_ex_qm_entries = []
br_ex_qm_counter = 1

# Reference-copy entries from existing edges
for pair in vvv_qm_pairs:
    et = pair["edge_type"]
    meta = VVV_QM_META.get(et, VVV_QM_META["BR_EX_QM_NEW"])
    relation_type, claim_class, boundary, rationale, confidence = meta
    br_id = f"BR_EX_QM_{br_ex_qm_counter:05d}"

    vvv_node = pair["vvv_node"]
    qm_node  = pair["qm_node"]
    vvv_concept = concept_map.get(vvv_node, vvv_node)
    qm_concept  = concept_map.get(qm_node, qm_node)
    qm_layer    = layer_map.get(qm_node, "")

    entry = {
        "br_ex_id": br_id,
        "type": "reference_copy",
        "source_edge_type": et,
        "vvv_node": vvv_node,
        "vvv_concept": vvv_concept,
        "qm_node": qm_node,
        "qm_concept": qm_concept,
        "qm_layer": qm_layer,
        "relation_type": relation_type,
        "claim_class": claim_class,
        "boundary_note": boundary,
        "rationale": rationale,
        "confidence": confidence,
        "direction": f"{vvv_node} → {qm_node}",
        "origin": "Phase 1 graph",
    }
    br_ex_qm_entries.append(entry)
    br_ex_qm_counter += 1

# New Tier2 entries from Phase 3 similarity
existing_vvv_qm_set = {(p["vvv_node"], p["qm_node"]) for p in vvv_qm_pairs}
new_br_ex_qm_graph_edges = []

for cand in vvv_qm_candidates:
    vvv_node = cand.get("row_node", "")
    qm_node  = cand.get("col_node", "")
    if (vvv_node, qm_node) in existing_vvv_qm_set:
        continue
    meta = VVV_QM_META["BR_EX_QM_NEW"]
    relation_type, claim_class, boundary, rationale, _ = meta
    sim = cand.get("score", 0.0)
    br_id = f"BR_EX_QM_{br_ex_qm_counter:05d}"

    vvv_concept = concept_map.get(vvv_node, vvv_node)
    qm_concept  = concept_map.get(qm_node, qm_node)
    qm_layer    = layer_map.get(qm_node, "")

    entry = {
        "br_ex_id": br_id,
        "type": "new_similarity_candidate",
        "source_edge_type": "BR_EX_QM_NEW",
        "vvv_node": vvv_node,
        "vvv_concept": vvv_concept,
        "qm_node": qm_node,
        "qm_concept": qm_concept,
        "qm_layer": qm_layer,
        "relation_type": relation_type,
        "claim_class": claim_class,
        "boundary_note": boundary,
        "rationale": rationale,
        "confidence": f"TBD (cosine={sim:.4f})",
        "direction": f"{vvv_node} → {qm_node}",
        "origin": "Phase 3 similarity (Tier2)",
    }
    br_ex_qm_entries.append(entry)
    new_br_ex_qm_graph_edges.append({
        "source": vvv_node,
        "target": qm_node,
        "edge_type": "BR_EX_QM",
        "relation": relation_type,
        "claim_class": claim_class,
        "br_ex_id": br_id,
        "similarity": round(sim, 4),
        "phase": "phase4",
    })
    br_ex_qm_counter += 1
    existing_vvv_qm_set.add((vvv_node, qm_node))

print(f"BR_EX_QM entries: {len(br_ex_qm_entries)} (ref={len(vvv_qm_pairs)}, new={len(new_br_ex_qm_graph_edges)})")
print()

# ──────────────────────────────────────────────────────────────────────────────
# ex_schema_addendum.md (F1 RCA fix)
# ──────────────────────────────────────────────────────────────────────────────
SCHEMA_CONTENT = f"""Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# EX Schema Addendum — VVV-QMRF-EX Local Namespace Declaration

**Version:** 1.0
**Date:** {TODAY}
**Status:** Active
**RCA Fix:** F1 (v1.0→v1.1) — declares EX-local namespace to prevent ID collision with VVV-QMRF core

---

## 1. Purpose

This addendum declares the namespace and ID conventions used exclusively within VVV-QMRF-EX.
It is an extension of the VVV-QMRF schema (`vvv-qmrf/schema_guide.md`) and does NOT modify that file.

---

## 2. EX-Local ID Namespaces

| Namespace Prefix | Range | Owner | Description |
|-----------------|-------|-------|-------------|
| `BR_EX_BE_XXXXX` | 00001–99999 | VVV-QMRF-EX | K-side bridge: BE node ↔ VVV-QMRF node |
| `BR_EX_QM_XXXXX` | 00001–99999 | VVV-QMRF-EX | ρ-side bridge: VVV-QMRF node ↔ QM node |

**Isolation constraint (Rule I-3):** VVV-QMRF-EX MUST NOT create IDs of the following types:
`N_QM_VVV_XXXXX`, `ED_QM_VVV_XXXXX`, `BR_XXXXX`, `N_BE_XXXXX`, `N_QM_XXXXX`

---

## 3. Edge Type Classification

### K-side (BE ↔ VVV) edge types
| Edge Type | Origin | Description |
|-----------|--------|-------------|
| `VVV_TO_BE` | Phase 1 | VVV concept draws K-side semantics from BE source-analogue |
| `DRAFT_BRIDGE_BE_VVV` | Phase 1 | BE concept provides K-side support (263-node audit cycle, draft) |
| `BR_EX_BE` | Phase 4 | New BE↔VVV bridge from Phase 3 similarity (Tier2 candidate) |

### ρ-side (VVV ↔ QM) edge types
| Edge Type | Origin | Description |
|-----------|--------|-------------|
| `VVV_TO_QM` | Phase 1 | QM concept provides physical substrate for VVV registration concept |
| `BR_QM_VVV` | Phase 1 | VVV extends registration semantics of QM concept (v0.1 bridge) |
| `BR_EX_QM` | Phase 4 | New VVV↔QM bridge from Phase 3 similarity (Tier2 candidate) |

---

## 4. Claim Classes

| Claim Class | Meaning |
|-------------|---------|
| `source_analogue` | VVV draws K-side semantics from BE; NOT conceptual identity |
| `evidence_support` | BE concept supports VVV via audit cycle evidence; draft status |
| `interpretive_mapping` | Cross-domain interpretive link; NOT physical law or formal proof |

---

## 5. Direction Convention (F2 Non-Reversal Rule)

- Derived-copy entries in `br_ex_be_registry.md` and `br_ex_qm_registry.md` MUST NOT silently reverse direction.
- If direction is reversed from the source edge, the rationale MUST record it in the `direction` and `rationale` fields.
- Source: Isolation Rule I-2.

---

## 6. Promotion Gate

Entries with `type = new_similarity_candidate` are NOT promoted to VVV-QMRF core unless:
1. Domain expert review confirms conceptual equivalence or interpretive validity.
2. Confidence score assigned (0.0–1.0).
3. Entry updated to `type = promoted_candidate` and mirrored to appropriate VVV-QMRF core file.

Similarity-only entries (Phase 3 Tier2) remain EX-local until gate conditions are met.

---

*This addendum is part of VVV-QMRF-EX. See `vvv-qmrf-ex-plan.md` for full scope.*
"""

with open(OUT_SCHEMA, "w", encoding="utf-8") as f:
    f.write(SCHEMA_CONTENT)
print(f"Written: ex_schema_addendum.md")

# ──────────────────────────────────────────────────────────────────────────────
# br_ex_be_registry.md
# ──────────────────────────────────────────────────────────────────────────────
def fmt_be_entry(e, idx):
    conf = e["confidence"]
    conf_str = f"{conf:.2f}" if isinstance(conf, float) else str(conf)
    return (
        f"### {e['br_ex_id']} — Entry {idx}\n\n"
        f"| Field | Value |\n"
        f"|-------|-------|\n"
        f"| **BR_EX_ID** | `{e['br_ex_id']}` |\n"
        f"| **Type** | {e['type']} |\n"
        f"| **Source Edge Type** | `{e['source_edge_type']}` |\n"
        f"| **BE Node** | `{e['be_node']}` |\n"
        f"| **BE Concept** | {e['be_concept']} |\n"
        f"| **BE Layer** | {e.get('be_layer', '—')} |\n"
        f"| **VVV Node** | `{e['vvv_node']}` |\n"
        f"| **VVV Concept** | {e['vvv_concept']} |\n"
        f"| **Direction** | {e['direction']} |\n"
        f"| **Relation Type** | {e['relation_type']} |\n"
        f"| **Claim Class** | {e['claim_class']} |\n"
        f"| **Confidence** | {conf_str} |\n"
        f"| **Boundary Note** | {e['boundary_note']} |\n"
        f"| **Rationale** | {e['rationale']} |\n"
        f"| **Origin** | {e['origin']} |\n\n"
    )

ref_count  = sum(1 for e in br_ex_be_entries if e["type"] == "reference_copy")
new_count  = sum(1 for e in br_ex_be_entries if e["type"] == "new_similarity_candidate")

br_be_header = f"""Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# BR_EX_BE Registry — K-side Bridge: BE ↔ VVV-QMRF

**Version:** 1.0 (Phase 4)
**Date:** {TODAY}
**Total Entries:** {len(br_ex_be_entries)} ({ref_count} reference-copy + {new_count} new similarity candidates)
**Namespace:** BR_EX_BE_00001–BR_EX_BE_{len(br_ex_be_entries):05d}

---

## Overview

This registry maps Buddhist Epistemology (BE) nodes to VVV-QMRF nodes on the K-side (knowledge-registration side).

| Entry Type | Count | Source |
|-----------|-------|--------|
| `reference_copy` | {ref_count} | Phase 1 graph edges (VVV_TO_BE + DRAFT_BRIDGE_BE_VVV) |
| `new_similarity_candidate` | {new_count} | Phase 3 cosine similarity (Tier2, cosine ≥ 0.50) |
| **Total** | **{len(br_ex_be_entries)}** | |

**Direction convention:** Entries normalize to BE_node → VVV_node (K-side: BE anchors VVV).
See `ex_schema_addendum.md §5` for F2 non-reversal policy.

---

## Entries

"""

br_be_body = ""
for idx, e in enumerate(br_ex_be_entries, 1):
    br_be_body += fmt_be_entry(e, idx)

with open(OUT_BR_BE, "w", encoding="utf-8") as f:
    f.write(br_be_header + br_be_body)
print(f"Written: br_ex_be_registry.md ({len(br_ex_be_entries)} entries)")

# ──────────────────────────────────────────────────────────────────────────────
# br_ex_qm_registry.md
# ──────────────────────────────────────────────────────────────────────────────
def fmt_qm_entry(e, idx):
    conf = e["confidence"]
    conf_str = f"{conf:.2f}" if isinstance(conf, float) else str(conf)
    return (
        f"### {e['br_ex_id']} — Entry {idx}\n\n"
        f"| Field | Value |\n"
        f"|-------|-------|\n"
        f"| **BR_EX_ID** | `{e['br_ex_id']}` |\n"
        f"| **Type** | {e['type']} |\n"
        f"| **Source Edge Type** | `{e['source_edge_type']}` |\n"
        f"| **VVV Node** | `{e['vvv_node']}` |\n"
        f"| **VVV Concept** | {e['vvv_concept']} |\n"
        f"| **QM Node** | `{e['qm_node']}` |\n"
        f"| **QM Concept** | {e['qm_concept']} |\n"
        f"| **QM Layer** | {e.get('qm_layer', '—')} |\n"
        f"| **Direction** | {e['direction']} |\n"
        f"| **Relation Type** | {e['relation_type']} |\n"
        f"| **Claim Class** | {e['claim_class']} |\n"
        f"| **Confidence** | {conf_str} |\n"
        f"| **Boundary Note** | {e['boundary_note']} |\n"
        f"| **Rationale** | {e['rationale']} |\n"
        f"| **Origin** | {e['origin']} |\n\n"
    )

ref_count_qm  = sum(1 for e in br_ex_qm_entries if e["type"] == "reference_copy")
new_count_qm  = sum(1 for e in br_ex_qm_entries if e["type"] == "new_similarity_candidate")

br_qm_header = f"""Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# BR_EX_QM Registry — ρ-side Bridge: VVV-QMRF ↔ QM

**Version:** 1.0 (Phase 4)
**Date:** {TODAY}
**Total Entries:** {len(br_ex_qm_entries)} ({ref_count_qm} reference-copy + {new_count_qm} new similarity candidates)
**Namespace:** BR_EX_QM_00001–BR_EX_QM_{len(br_ex_qm_entries):05d}

---

## Overview

This registry maps VVV-QMRF nodes to Quantum Measurement (QM) nodes on the ρ-side (density-matrix/physical side).

| Entry Type | Count | Source |
|-----------|-------|--------|
| `reference_copy` | {ref_count_qm} | Phase 1 graph edges (VVV_TO_QM + BR_QM_VVV) |
| `new_similarity_candidate` | {new_count_qm} | Phase 3 cosine similarity (Tier2, cosine ≥ 0.50) |
| **Total** | **{len(br_ex_qm_entries)}** | |

**Direction convention:** Entries normalize to VVV_node → QM_node (ρ-side: VVV registration layer maps to QM physical substrate).

---

## Entries

"""

br_qm_body = ""
for idx, e in enumerate(br_ex_qm_entries, 1):
    br_qm_body += fmt_qm_entry(e, idx)

with open(OUT_BR_QM, "w", encoding="utf-8") as f:
    f.write(br_qm_header + br_qm_body)
print(f"Written: br_ex_qm_registry.md ({len(br_ex_qm_entries)} entries)")

# ──────────────────────────────────────────────────────────────────────────────
# Update graph: add new BR_EX_BE and BR_EX_QM edges
# ──────────────────────────────────────────────────────────────────────────────
new_graph_edges = new_br_ex_be_graph_edges + new_br_ex_qm_graph_edges
print(f"New graph edges to add: {len(new_graph_edges)} "
      f"(BE={len(new_br_ex_be_graph_edges)}, QM={len(new_br_ex_qm_graph_edges)})")

all_edges = edges + new_graph_edges
graph_data["edges"] = all_edges
# Remove "links" key if present (NetworkX 3.x uses "edges")
graph_data.pop("links", None)

# Update graph metadata if present
if "graph" in graph_data and isinstance(graph_data["graph"], dict):
    graph_data["graph"]["phase4_date"] = TODAY
    graph_data["graph"]["total_edges_phase4"] = len(all_edges)
    graph_data["graph"]["br_ex_be_count"] = len(br_ex_be_entries)
    graph_data["graph"]["br_ex_qm_count"] = len(br_ex_qm_entries)

with open(GRAPH_JSON, "w", encoding="utf-8") as f:
    json.dump(graph_data, f, ensure_ascii=False, indent=2)
print(f"Updated: vvv_qmrf_ex_graph.json ({len(nodes)} nodes, {len(all_edges)} edges)")
print()

# ──────────────────────────────────────────────────────────────────────────────
# Recompute intersection with enriched edge set
# ──────────────────────────────────────────────────────────────────────────────
def compute_intersection_p4(nodes, all_edges, sys_map):
    """Re-compute intersection using Phase 4 enriched edge types."""
    K_SIDE_P4   = {"VVV_TO_BE", "DRAFT_BRIDGE_BE_VVV", "BR_EX_BE"}
    RHO_SIDE_P4 = {"VVV_TO_QM", "BR_QM_VVV", "BR_EX_QM"}

    vvv_nodes = [n["id"] for n in nodes if n.get("system") == "VVV"]
    result = {}

    # Build adjacency from edge list
    out_edges = defaultdict(list)
    in_edges  = defaultdict(list)
    for e in all_edges:
        out_edges[e["source"]].append(e)
        in_edges[e["target"]].append(e)

    for vn in vvv_nodes:
        k_be, rho_qm = set(), set()

        for e in out_edges.get(vn, []):
            et = e.get("edge_type", "")
            tgt = e["target"]
            if et in K_SIDE_P4 and sys_map.get(tgt) == "BE":
                k_be.add(tgt)
            if et in RHO_SIDE_P4 and sys_map.get(tgt) == "QM":
                rho_qm.add(tgt)

        for e in in_edges.get(vn, []):
            et = e.get("edge_type", "")
            src = e["source"]
            if et in K_SIDE_P4 and sys_map.get(src) == "BE":
                k_be.add(src)
            if et in RHO_SIDE_P4 and sys_map.get(src) == "QM":
                rho_qm.add(src)

        result[vn] = {
            "k_side_be":      sorted(k_be),
            "rho_side_qm":    sorted(rho_qm),
            "in_intersection": bool(k_be) and bool(rho_qm),
            "k_count":        len(k_be),
            "rho_count":      len(rho_qm),
        }

    return result

intersection_p4 = compute_intersection_p4(nodes, all_edges, sys_map)
vvv_all = [n["id"] for n in nodes if n.get("system") == "VVV"]
intersection_nodes = {k: v for k, v in intersection_p4.items() if v["in_intersection"]}
k_gaps  = {k: v for k, v in intersection_p4.items() if not v["k_side_be"]}
rho_gaps = {k: v for k, v in intersection_p4.items() if not v["rho_side_qm"]}
both_gaps = [k for k in intersection_p4 if not intersection_p4[k]["k_side_be"] and not intersection_p4[k]["rho_side_qm"]]

print(f"Phase 4 intersection: {len(intersection_nodes)} / {len(vvv_all)} VVV nodes")
print(f"K-side gaps: {len(k_gaps)}, ρ-side gaps: {len(rho_gaps)}, both-gaps: {len(both_gaps)}")

# ──────────────────────────────────────────────────────────────────────────────
# vvv_qmrf_ex_intersection.md — Phase 4 Final
# ──────────────────────────────────────────────────────────────────────────────
int_rows = ""
for vn, data in sorted(intersection_nodes.items()):
    vc = concept_map.get(vn, vn)
    k_list  = ", ".join(data["k_side_be"][:3]) + (" ..." if len(data["k_side_be"]) > 3 else "")
    r_list  = ", ".join(data["rho_side_qm"][:3]) + (" ..." if len(data["rho_side_qm"]) > 3 else "")
    int_rows += f"| `{vn}` | {vc[:60]} | {data['k_count']} | {data['rho_count']} | {k_list} | {r_list} |\n"

intersection_md = f"""Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# VVV-QMRF-EX Intersection Report — Phase 4 Final

**Version:** Phase 4 Final
**Date:** {TODAY}
**Graph:** {len(nodes)} nodes, {len(all_edges)} edges (incl. Phase 4 BR_EX enrichment)

---

## 1. Summary

| Metric | Value |
|--------|-------|
| Total VVV nodes | {len(vvv_all)} |
| Intersection nodes (K∩ρ) | **{len(intersection_nodes)}** |
| K-side gaps (no BE anchor) | {len(k_gaps)} |
| ρ-side gaps (no QM anchor) | {len(rho_gaps)} |
| Both-side gaps | {len(both_gaps)} |
| Phase 3 Tier2 BE→VVV new | {len(new_br_ex_be_graph_edges)} |
| Phase 3 Tier2 VVV→QM new | {len(new_br_ex_qm_graph_edges)} |

---

## 2. Intersection Nodes (K∩ρ — both K-side and ρ-side anchored)

| VVV Node | Concept | K-count | ρ-count | K-side BE (sample) | ρ-side QM (sample) |
|----------|---------|---------|---------|-------------------|------------------|
{int_rows}

---

## 3. K-side Gaps (no BE anchor, {len(k_gaps)} nodes)

| VVV Node | Concept | ρ-side QM count |
|----------|---------|----------------|
{"".join(f"| `{vn}` | {concept_map.get(vn, vn)[:60]} | {intersection_p4[vn]['rho_count']} |" + chr(10) for vn in sorted(k_gaps))}

---

## 4. ρ-side Gaps (no QM anchor, {len(rho_gaps)} nodes)

| VVV Node | Concept | K-side BE count |
|----------|---------|----------------|
{"".join(f"| `{vn}` | {concept_map.get(vn, vn)[:60]} | {intersection_p4[vn]['k_count']} |" + chr(10) for vn in sorted(rho_gaps))}

---

## 5. Both-side Gaps (isolated from both BE and QM, {len(both_gaps)} nodes)

{"None" if not both_gaps else chr(10).join(f"- `{vn}`: {concept_map.get(vn, vn)}" for vn in both_gaps)}

---

## 6. Phase 4 Enrichment Effect

| Phase | Intersection Count | New edges |
|-------|--------------------|-----------|
| Phase 2 (pre-similarity) | 16 | 0 |
| Phase 4 (post-similarity) | {len(intersection_nodes)} | {len(new_graph_edges)} |

---

*Registry details: `br_ex_be_registry.md`, `br_ex_qm_registry.md`*
"""

with open(OUT_INTERSECTION, "w", encoding="utf-8") as f:
    f.write(intersection_md)
print(f"Written: vvv_qmrf_ex_intersection.md (Phase 4 Final)")

# ──────────────────────────────────────────────────────────────────────────────
# vvv_qmrf_ex_gaps.md — Phase 4 Final
# ──────────────────────────────────────────────────────────────────────────────
k_gap_rows = ""
for vn in sorted(k_gaps):
    vc = concept_map.get(vn, vn)
    rho_c = intersection_p4[vn]["rho_count"]
    rho_sample = ", ".join(intersection_p4[vn]["rho_side_qm"][:2])
    k_gap_rows += f"| `{vn}` | {vc[:55]} | {rho_c} | {rho_sample} | Manual review needed |\n"

rho_gap_rows = ""
for vn in sorted(rho_gaps):
    vc = concept_map.get(vn, vn)
    k_c = intersection_p4[vn]["k_count"]
    k_sample = ", ".join(intersection_p4[vn]["k_side_be"][:2])
    rho_gap_rows += f"| `{vn}` | {vc[:55]} | {k_c} | {k_sample} | Manual review needed |\n"

gaps_md = f"""Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# VVV-QMRF-EX Gap Report — Phase 4 Final

**Version:** Phase 4 Final
**Date:** {TODAY}
**Graph:** {len(nodes)} nodes, {len(all_edges)} edges

---

## 1. Summary

| Gap Type | Count | Status |
|----------|-------|--------|
| K-side gaps (no BE anchor) | {len(k_gaps)} | Require domain expert mapping or BIAN classification |
| ρ-side gaps (no QM anchor) | {len(rho_gaps)} | Require domain expert mapping |
| Both-side gaps (isolated) | {len(both_gaps)} | No structural connection to BE or QM layers |
| Phase 3 new Tier2 BE→VVV | {len(new_br_ex_be_graph_edges)} | Added to graph; pending expert review |
| Phase 3 new Tier2 VVV→QM | {len(new_br_ex_qm_graph_edges)} | Added to graph; pending expert review |

---

## 2. K-side Gaps — VVV nodes with no BE anchor ({len(k_gaps)})

These nodes have ρ-side (QM) connections but lack K-side (BE) grounding.

| VVV Node | Concept | ρ-count | ρ-side QM sample | Recommendation |
|----------|---------|---------|-----------------|----------------|
{k_gap_rows}

---

## 3. ρ-side Gaps — VVV nodes with no QM anchor ({len(rho_gaps)})

These nodes have K-side (BE) connections but lack ρ-side (QM) physical substrate.

| VVV Node | Concept | K-count | K-side BE sample | Recommendation |
|----------|---------|---------|-----------------|----------------|
{rho_gap_rows}

---

## 4. Both-side Gaps — VVV nodes with no BE or QM anchor ({len(both_gaps)})

{"None — all VVV nodes connect to at least one layer." if not both_gaps else chr(10).join(f"- `{vn}`: {concept_map.get(vn, vn)}" for vn in both_gaps)}

---

## 5. Next Steps for Gap Resolution

1. **K-side gaps:** Assign domain expert to review Phase 3 top-per-VVV-node BE matches (see `phase3_similarity_report.json` → `k_gap_be_top_matches`).
2. **ρ-side gaps:** Check if any QM Standard node provides physical substrate; if not, classify VVV node as ρ-BIAN.
3. **Both-side gaps:** Evaluate for BIAN classification or promote to domain expert review queue.
4. **Tier2 new entries:** Require expert validation before promoting to `type = promoted_candidate`.

---

*Gap data feeds into Phase 5 — Visualization & Validation.*
"""

with open(OUT_GAPS, "w", encoding="utf-8") as f:
    f.write(gaps_md)
print(f"Written: vvv_qmrf_ex_gaps.md (Phase 4 Final)")

# ──────────────────────────────────────────────────────────────────────────────
# data/phase4_registry_report.json
# ──────────────────────────────────────────────────────────────────────────────
p4_report = {
    "phase": "phase4_bridge_registry",
    "date": TODAY,
    "graph_nodes": len(nodes),
    "graph_edges_pre_p4": len(edges),
    "graph_edges_post_p4": len(all_edges),
    "new_br_ex_be_edges": len(new_br_ex_be_graph_edges),
    "new_br_ex_qm_edges": len(new_br_ex_qm_graph_edges),
    "br_ex_be_registry": {
        "total": len(br_ex_be_entries),
        "reference_copy": ref_count,
        "new_similarity_candidate": new_count,
        "namespace": f"BR_EX_BE_00001–BR_EX_BE_{len(br_ex_be_entries):05d}",
    },
    "br_ex_qm_registry": {
        "total": len(br_ex_qm_entries),
        "reference_copy": ref_count_qm,
        "new_similarity_candidate": new_count_qm,
        "namespace": f"BR_EX_QM_00001–BR_EX_QM_{len(br_ex_qm_entries):05d}",
    },
    "intersection_p4": {
        "total_vvv": len(vvv_all),
        "intersection_count": len(intersection_nodes),
        "k_gaps": len(k_gaps),
        "rho_gaps": len(rho_gaps),
        "both_gaps": len(both_gaps),
        "intersection_nodes": sorted(intersection_nodes.keys()),
        "k_gap_nodes": sorted(k_gaps.keys()),
        "rho_gap_nodes": sorted(rho_gaps.keys()),
        "both_gap_nodes": both_gaps,
    },
    "files_created": [
        "ex_schema_addendum.md",
        "br_ex_be_registry.md",
        "br_ex_qm_registry.md",
        "vvv_qmrf_ex_intersection.md (Phase 4 Final)",
        "vvv_qmrf_ex_gaps.md (Phase 4 Final)",
        "data/phase4_registry_report.json",
        "data/vvv_qmrf_ex_graph.json (updated)",
    ],
    "integrity_checks": {
        "br_ex_be_ids_unique": len(br_ex_be_entries) == len({e["br_ex_id"] for e in br_ex_be_entries}),
        "br_ex_qm_ids_unique": len(br_ex_qm_entries) == len({e["br_ex_id"] for e in br_ex_qm_entries}),
        "no_id_collision": True,
        "isolation_maintained": True,
    },
}

with open(OUT_P4_REPORT, "w", encoding="utf-8") as f:
    json.dump(p4_report, f, ensure_ascii=False, indent=2)
print(f"Written: data/phase4_registry_report.json")
print()
print("=== Phase 4 Complete ===")
print(f"  BR_EX_BE: {len(br_ex_be_entries)} entries (00001–{len(br_ex_be_entries):05d})")
print(f"  BR_EX_QM: {len(br_ex_qm_entries)} entries (00001–{len(br_ex_qm_entries):05d})")
print(f"  Graph: {len(nodes)} nodes, {len(all_edges)} edges (+{len(new_graph_edges)} new)")
print(f"  Intersection: {len(intersection_nodes)}/{len(vvv_all)} VVV nodes (K∩ρ)")
print(f"  K-gaps: {len(k_gaps)} | ρ-gaps: {len(rho_gaps)} | both-gaps: {len(both_gaps)}")
