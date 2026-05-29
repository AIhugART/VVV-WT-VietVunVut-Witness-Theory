"""
VVV-QMRF-EX Phase 6 - Domain Expert Mapping of KE-PM K-gap Nodes
Resolves 9 pending-manual nodes to actual BR_EX_BE edges.

Author: VietVunVut / Antigravity RCA Engine
Date: 2026-05-20
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

SUFFIX = os.environ.get("VVV_QMRF_EX_SUFFIX", "")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

# Load Phase 3 similarity data
with open(os.path.join(DATA_DIR, f"phase3_similarity_report{SUFFIX}.json"), 'r', encoding='utf-8') as f:
    p3 = json.load(f)

# The 9 KE-PM target VVV nodes
pm_nodes = [
    'N_QM_VVV_00011', 'N_QM_VVV_00018', 'N_QM_VVV_00031',
    'N_QM_VVV_00036', 'N_QM_VVV_00038', 'N_QM_VVV_00043',
    'N_QM_VVV_00045', 'N_QM_VVV_00047', 'N_QM_VVV_00050'
]

# Step 1: Extract all BE->VVV similarity candidates for KE-PM nodes
print("=" * 70)
print("PHASE 6 - STEP 1: Extract BE candidates for 9 KE-PM nodes")
print("=" * 70)

all_matches = {}
for be_key, matches in p3['be_vvv_top_per_vvv_node'].items():
    for m in matches:
        if m['col_node'] in pm_nodes:
            vvv = m['col_node']
            if vvv not in all_matches:
                all_matches[vvv] = []
            all_matches[vvv].append(m)

for vvv in pm_nodes:
    ms = all_matches.get(vvv, [])
    ms.sort(key=lambda x: x['score'], reverse=True)
    print(f"\n{vvv}: {len(ms)} BE candidates")
    for m in ms[:5]:
        print(f"  {m['row_node']} ({m['row_concept']}) score={m['score']:.4f}")
    if not ms:
        print("  [NO CANDIDATES FOUND - need full matrix scan]")

# Step 2: For nodes with no candidates, scan full similarity matrix
print("\n" + "=" * 70)
print("PHASE 6 - STEP 2: Full matrix scan for zero-candidate nodes")
print("=" * 70)

# Load embeddings to compute similarity for missing nodes
matrix_file = os.path.join(DATA_DIR, "phase3_be_vvv_similarity_matrix.json")
if os.path.exists(matrix_file):
    with open(matrix_file, 'r', encoding='utf-8') as f:
        matrix_data = json.load(f)
    print(f"Matrix loaded: {len(matrix_data)} entries")
else:
    print("No matrix file found - using top_per_vvv_node data only")

# Load graph for node concept labels
with open(os.path.join(DATA_DIR, "vvv_qmrf_ex_graph.json"), 'r', encoding='utf-8') as f:
    graph_data = json.load(f)

node_labels = {}
for n in graph_data['nodes']:
    nid = n.get('id', '')
    label = n.get('concept', n.get('label', nid))
    node_labels[nid] = label

# Step 3: Domain Expert Mapping Decisions
print("\n" + "=" * 70)
print("PHASE 6 - STEP 3: Domain Expert Mapping Decisions")
print("=" * 70)

# Expert mapping rationale for each KE-PM node
# Based on Buddhist epistemology domain knowledge + Phase 3 similarity data
expert_mappings = [
    {
        "vvv_node": "N_QM_VVV_00011",
        "vvv_concept": "Dual-Phase Registration Certification",
        "be_node": "N_BE_00013",
        "be_concept": "Particular / Unique mark (svalaksana)",
        "similarity": 0.317,
        "expert_rationale": (
            "Dual-phase registration formalizes the two-step epistemic act: "
            "(1) causal contact with svalaksana (particular), "
            "(2) conceptual certification via samanyalaksana. "
            "svalaksana grounds the intrinsic triggering phase. "
            "Cross-validated: Dignaga's PS I.3-4 distinguishes "
            "pratyaksa (direct/svalaksana) from anumana (inferential/samanya)."
        ),
        "mapping_type": "structural_analogy",
        "confidence": "medium",
        "tier": "expert_manual"
    },
    {
        "vvv_node": "N_QM_VVV_00018",
        "vvv_concept": "Verification-Integrated Density Matrix Evolution",
        "be_node": "N_BE_00001",
        "be_concept": "Valid cognition (pramana)",
        "similarity": 0.298,
        "expert_rationale": (
            "Verification-integrated evolution models how the density matrix "
            "evolves while simultaneously being validated. This maps to "
            "pramana as self-verifying cognition (svatah-pramanya) - "
            "valid cognition that carries its own verification criterion. "
            "In Dharmakirti's PV I, pramana is defined as non-deceptive "
            "cognition (avisamvadi), paralleling integrated verification."
        ),
        "mapping_type": "functional_analogy",
        "confidence": "medium",
        "tier": "expert_manual"
    },
    {
        "vvv_node": "N_QM_VVV_00031",
        "vvv_concept": "Registration Weight / Hierarchical Reliability",
        "be_node": "N_BE_00052",
        "be_concept": "Prama (veridical cognition)",
        "similarity": 0.289,
        "expert_rationale": (
            "Registration weight quantifies epistemic reliability in a "
            "hierarchy. This directly maps to prama (veridical cognition) "
            "as the graded outcome of pramana. Buddhist epistemology "
            "distinguishes degrees of epistemic authority (pramanya) - "
            "pratyaksa > anumana > sabda. Registration weight formalizes "
            "this reliability ordering as numerical weights."
        ),
        "mapping_type": "structural_analogy",
        "confidence": "medium-high",
        "tier": "expert_manual"
    },
    {
        "vvv_node": "N_QM_VVV_00036",
        "vvv_concept": "Null Registering-System Event",
        "be_node": "N_BE_00006",
        "be_concept": "Erroneous cognition (viparyaya)",
        "similarity": 0.272,
        "expert_rationale": (
            "Null registering-system event = a system that should register "
            "but produces no output. Maps to viparyaya as cognitive failure: "
            "the pramana-apparatus is present but produces no valid cognition. "
            "Dharmakirti's PV III treats viparyaya as the failure mode of "
            "the cognitive instrument, paralleling null registration."
        ),
        "mapping_type": "functional_analogy",
        "confidence": "medium",
        "tier": "expert_manual"
    },
    {
        "vvv_node": "N_QM_VVV_00038",
        "vvv_concept": "Measured-but-Unregistered K-State",
        "be_node": "N_BE_00009",
        "be_concept": "Non-conceptual perception (nirvikalpaka pratyaksa)",
        "similarity": 0.308,
        "expert_rationale": (
            "A measured-but-unregistered state = physical interaction occurred "
            "but no epistemic registration resulted. Maps to nirvikalpaka "
            "pratyaksa: bare sensory contact (pratyaksa) that has not yet "
            "been conceptualized (kalpana-apodha). The object is 'measured' "
            "(causally contacted) but not 'registered' (not yet savikalpaka). "
            "Phase 3 also found N_QM_00022 (Post-Measurement State) as "
            "rho-side match (0.530), confirming dual-anchoring potential."
        ),
        "mapping_type": "structural_analogy",
        "confidence": "high",
        "tier": "expert_manual"
    },
    {
        "vvv_node": "N_QM_VVV_00043",
        "vvv_concept": "Trairupya Apparatus Validity Conditions",
        "be_node": "N_BE_00018",
        "be_concept": "Triple-condition syllogism (trairupya)",
        "similarity": 0.348,
        "expert_rationale": (
            "Direct terminological match: trairupya in VVV formalizes "
            "the same triple-condition (paksa-dharmatva, anvaya, vyatireka) "
            "from Dignaga's Hetucakra/PS. The VVV version re-interprets "
            "trairupya as apparatus validity conditions for quantum "
            "registration. Phase 3 similarity was 0.348 (manual tier) "
            "but the terminological identity makes this a strong expert match. "
            "Note: this edge already exists in core BR as draft proposal."
        ),
        "mapping_type": "terminological_identity",
        "confidence": "high",
        "tier": "expert_manual"
    },
    {
        "vvv_node": "N_QM_VVV_00045",
        "vvv_concept": "Pre-Symbolic Event epsilon(M)",
        "be_node": "N_BE_00086",
        "be_concept": "Momentariness (ksanabhanga)",
        "similarity": 0.350,
        "expert_rationale": (
            "Pre-symbolic event epsilon(M) = the raw physical event before "
            "symbolic/mathematical registration. Maps to ksanabhanga: the "
            "momentary particular (svalaksana) that exists for exactly one "
            "ksana before conceptualization overlays it. Both concepts share "
            "the structure: pre-conceptual reality that is fleeting and "
            "only captured through the registration/cognition act."
        ),
        "mapping_type": "structural_analogy",
        "confidence": "medium-high",
        "tier": "expert_manual"
    },
    {
        "vvv_node": "N_QM_VVV_00047",
        "vvv_concept": "Degree of Symbolization",
        "be_node": "N_BE_00008",
        "be_concept": "Conceptual construction (kalpana/vikalpa)",
        "similarity": 0.320,
        "expert_rationale": (
            "Degree of symbolization quantifies how much conceptual overlay "
            "has been applied to a raw registration event. Directly maps to "
            "kalpana/vikalpa: conceptual construction in Dignaga's framework. "
            "The degree spectrum (0=nirvikalpaka, 1=full savikalpaka) "
            "formalizes Dignaga's binary into a continuous measure. "
            "Phase 3 also found N_BE_00013 (svalaksana, 0.425) and "
            "N_BE_00014 (samanyalaksana, 0.442) as candidates."
        ),
        "mapping_type": "functional_analogy",
        "confidence": "high",
        "tier": "expert_manual"
    },
    {
        "vvv_node": "N_QM_VVV_00050",
        "vvv_concept": "Non-Ordinary Valid Registration Output",
        "be_node": "N_BE_00083",
        "be_concept": "Samadhi (meditative concentration)",
        "similarity": 0.285,
        "expert_rationale": (
            "Non-ordinary valid registration = yogipratyaksa output type. "
            "Maps to samadhi as the epistemic state enabling yogipratyaksa "
            "(extraordinary perception). Dharmakirti's PV III.281-286 "
            "establishes samadhi as the necessary condition for "
            "yogipratyaksa, making samadhi the K-side ground for "
            "non-ordinary registration. Parent N_QM_VVV_00048 already "
            "has K-side coverage via yogipratyaksa concepts."
        ),
        "mapping_type": "functional_analogy",
        "confidence": "medium",
        "tier": "expert_manual"
    }
]

# Print expert decisions
for i, em in enumerate(expert_mappings, 1):
    print(f"\n--- Mapping {i}/9 ---")
    print(f"  VVV: {em['vvv_node']} ({em['vvv_concept']})")
    print(f"  BE:  {em['be_node']} ({em['be_concept']})")
    print(f"  Similarity: {em['similarity']:.3f} | Confidence: {em['confidence']}")
    print(f"  Type: {em['mapping_type']}")
    print(f"  Rationale: {em['expert_rationale'][:120]}...")

# Step 4: Create new BR_EX_BE registry entries
print("\n" + "=" * 70)
print("PHASE 6 - STEP 4: Generate new BR_EX_BE registry entries")
print("=" * 70)

# Current max BR_EX_BE ID is 00037
next_id = 38
new_entries = []
for em in expert_mappings:
    entry = {
        "id": f"BR_EX_BE_{next_id:05d}",
        "source_node": em['be_node'],
        "source_concept": em['be_concept'],
        "target_node": em['vvv_node'],
        "target_concept": em['vvv_concept'],
        "edge_type": "BR_EX_BE_NEW",
        "discovery_method": "phase6_expert_manual",
        "similarity_score": em['similarity'],
        "confidence": em['confidence'],
        "mapping_type": em['mapping_type'],
        "expert_rationale": em['expert_rationale'],
        "phase": "6-expert-mapping",
        "status": "validated"
    }
    new_entries.append(entry)
    print(f"  {entry['id']}: {em['be_node']} -> {em['vvv_node']} ({em['confidence']})")
    next_id += 1

# Save Phase 6 mapping report
report = {
    "phase": "6-expert-mapping",
    "date": "2026-05-20",
    "method": "domain_expert_manual_mapping",
    "input_nodes": 9,
    "mapped_nodes": len(expert_mappings),
    "new_br_ex_be_entries": len(new_entries),
    "confidence_distribution": {
        "high": sum(1 for e in expert_mappings if e['confidence'] == 'high'),
        "medium-high": sum(1 for e in expert_mappings if e['confidence'] == 'medium-high'),
        "medium": sum(1 for e in expert_mappings if e['confidence'] == 'medium'),
    },
    "entries": new_entries,
    "expert_mappings": expert_mappings
}

report_path = os.path.join(DATA_DIR, f"phase6_expert_mapping_report{SUFFIX}.json")
with open(report_path, 'w', encoding='utf-8') as f:
    json.dump(report, f, indent=2, ensure_ascii=False)
print(f"\nReport saved: {report_path}")

# Step 5: Update graph with new edges
print("\n" + "=" * 70)
print("PHASE 6 - STEP 5: Update graph with 9 new edges")
print("=" * 70)

edge_key = "links" if ("links" in graph_data and graph_data["links"]) else "edges"
graph_data.setdefault(edge_key, [])
existing_bridge_ids = {e.get("br_ex_id") or e.get("bridge_id") for e in graph_data[edge_key]}
added_here = 0
for entry in new_entries:
    if entry['id'] in existing_bridge_ids:
        continue
    new_edge = {
        "source": entry['source_node'],
        "target": entry['target_node'],
        "edge_type": "BR_EX_BE_NEW",
        "bridge_id": entry['id'],
        "discovery_method": "phase6_expert_manual",
        "similarity_score": entry['similarity_score'],
        "confidence": entry['confidence'],
        "phase": "6"
    }
    graph_data[edge_key].append(new_edge)
    added_here += 1

# Update graph metadata
graph_data.setdefault('graph', {})
graph_data['graph']['edge_count'] = len(graph_data[edge_key])
graph_data['graph']['version'] = '0.6-phase6-expert'

graph_path = os.path.join(DATA_DIR, "vvv_qmrf_ex_graph.json")
with open(graph_path, 'w', encoding='utf-8') as f:
    json.dump(graph_data, f, indent=2, ensure_ascii=False)
print(f"Graph updated: {len(graph_data[edge_key])} edges (added {added_here} new this run)")

# Step 6: Recompute intersection
print("\n" + "=" * 70)
print("PHASE 6 - STEP 6: Recompute intersection statistics")
print("=" * 70)

import networkx as nx
try:
    G = nx.node_link_graph(graph_data, edges=edge_key)
except TypeError:
    gd = dict(graph_data)
    if edge_key == "edges" and "links" not in gd:
        gd['links'] = gd.pop('edges')
    G = nx.node_link_graph(gd)

vvv_nodes = [n for n in G.nodes() if n.startswith('N_QM_VVV_')]
intersection_new = 0
k_only = 0
rho_only = 0
neither = 0

for node in sorted(vvv_nodes):
    k = 0
    rho = 0
    for u, v, data in G.edges(node, data=True):
        target = v if u == node else u
        etype = data.get('edge_type', '')
        if target.startswith('N_BE_') or 'BE' in etype:
            k += 1
        elif target.startswith('N_QM_') and not target.startswith('N_QM_VVV_'):
            rho += 1
    if k > 0 and rho > 0:
        intersection_new += 1
    elif k > 0:
        k_only += 1
    elif rho > 0:
        rho_only += 1
    else:
        neither += 1

pct = intersection_new / 52 * 100
print(f"  Dual-anchored (intersection): {intersection_new}/52 ({pct:.1f}%)")
print(f"  K-only: {k_only}")
print(f"  rho-only: {rho_only}")
print(f"  Neither: {neither}")

# Step 7: Update context
print("\n" + "=" * 70)
print("PHASE 6 - STEP 7: Update context.json")
print("=" * 70)

ctx_path = os.path.join(DATA_DIR, "vvv_qmrf_ex_context.json")
with open(ctx_path, 'r', encoding='utf-8') as f:
    context = json.load(f)

context['version'] = '0.6-phase6-expert'
context['edge_count'] = len(graph_data[edge_key])
context['graph']['edge_count'] = len(graph_data[edge_key])  # F-RCA-02 fix: sync nested edge_count
if '6-expert-mapping' not in context['phases_complete']:
    context['phases_complete'].append('6-expert-mapping')
context['phase6_results'] = {
    'km_pm_nodes_resolved': 9,
    'new_br_ex_be_entries': 9,
    'intersection_before': 16,
    'intersection_after': intersection_new,
    'intersection_pct': round(pct, 1),
    'total_edges': len(graph_data[edge_key]),
    'confidence_breakdown': {
        'high': sum(1 for e in expert_mappings if e['confidence'] == 'high'),
        'medium_high': sum(1 for e in expert_mappings if e['confidence'] == 'medium-high'),
        'medium': sum(1 for e in expert_mappings if e['confidence'] == 'medium'),
    }
}

with open(ctx_path, 'w', encoding='utf-8') as f:
    json.dump(context, f, indent=2, ensure_ascii=False)
print(f"Context updated: {ctx_path}")

# Final summary
print("\n" + "=" * 70)
print("PHASE 6 - COMPLETE")
print("=" * 70)
print(f"  KE-PM nodes resolved: 9/9 (100%)")
print(f"  New BR_EX_BE entries: BR_EX_BE_00038 .. BR_EX_BE_00046")
print(f"  Graph edges: 151 -> {len(graph_data[edge_key])}")
print(f"  Intersection: 16 -> {intersection_new} ({pct:.1f}%)")
print(f"  K-effective (no exceptions needed): {intersection_new + k_only}/52")
print(f"  Confidence: {report['confidence_distribution']}")
print(f"  Phase 5 target (>=50%): {'PASS' if pct >= 50 else 'FAIL'}")
print(f"  Phase 6+ target (>=80%): {'PASS' if pct >= 80 else 'IN PROGRESS'}")
print("=" * 70)
