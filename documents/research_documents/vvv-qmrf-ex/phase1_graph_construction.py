"""
VVV-QMRF-EX Phase 1 — Graph Construction
Plan: vvv-qmrf-ex-plan.md §7 Phase 1 (Steps 1.1–1.6)
Execution: C:/Users/PC/AppData/Local/Programs/Python/Python312/python.exe

Steps:
  1.1 Parse 263 BE nodes  (source_snapshot/system_be/system_be_full.md)
  1.2 Parse  62 VVV nodes (source_snapshot/vvv_qmrf_core/node_QM_VVV.md)
  1.3 Parse 105 QM nodes  (source_snapshot/system_qm/system_qm_full.md)
  1.4 Parse 131 VVV edges + 15 BR bridges + 19 draft bridges from source_snapshot
  1.5 Build NetworkX MultiDiGraph → save vvv_qmrf_ex_graph.json
  1.6 Validate: zero dangling edge refs (orphan nodes permitted per F3 RCA fix)
"""

import os
import re
import json
import sys
from pathlib import Path
import networkx as nx
from networkx.readwrite import json_graph

# Force UTF-8 output on Windows console
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SUFFIX = os.environ.get("VVV_QMRF_EX_SUFFIX", "")

# ── Paths ────────────────────────────────────────────────────────────────────
BASE = Path("c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement")
OUT  = BASE / "documents/research_documents/vvv-qmrf-ex/data"

SNAPSHOT = BASE / "documents/research_documents/vvv-qmrf-ex/source_snapshot"

BE_SOT       = SNAPSHOT / "system_be/system_be_full.md"
VVV_NODES    = SNAPSHOT / "vvv_qmrf_core/node_QM_VVV.md"
QM_SOT       = SNAPSHOT / "system_qm/system_qm_full.md"
VVV_EDGES    = SNAPSHOT / "vvv_qmrf_core/edge_QM_VVV.md"
BRIDGE_FILE  = SNAPSHOT / "vvv_qmrf_core/bridge_QM_standard_to_VVV_QMRF.md"
DRAFT_FILE   = SNAPSHOT / "be_263_audit/BE_QM_Bridge_Registry_Consolidated_Draft_Batch_BCDEF.md"

# BIAN → primary VVV root node (derived from node_QM_VVV.md BIAN annotations)
BIAN_TO_VVV = {
    "BIAN-4":  "N_QM_VVV_00021",   # Registration Lock (first BIAN-4 root)
    "BIAN-9":  "N_QM_VVV_00020",   # Validated Absence Registration
    "BIAN-14": "N_QM_VVV_00042",   # Tripartite Registration Validity Matrix
    "BIAN-15": "N_QM_VVV_00001",   # Contrapositive Quantum Evidence
    "BIAN-16": "N_QM_VVV_00027",   # Registration Self-Completion Matrix
}

# ── Node code regex patterns ──────────────────────────────────────────────────
RE_BE_CODE  = re.compile(r'\bN_BE_\d{5}\b')
RE_VVV_CODE = re.compile(r'\bN_QM_VVV_\d{5}\b')
RE_QM_CODE  = re.compile(r'\bN_QM_\d{5}\b')


# ── 1.1  Parse BE nodes ───────────────────────────────────────────────────────
def parse_be_nodes(path: Path) -> dict:
    """
    Parse N_BE_XXXXX nodes from system_be_full.md markdown table.
    Table columns (0-indexed after splitting on '|'):
      [1]=No  [2]=Node code  [3]=Layer  [4]=Concept  ...
    Deduplicate by node code (first occurrence wins).
    """
    nodes = {}
    row_re = re.compile(r'^\|\s*\d+\s*\|\s*(N_BE_\d{5})\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|')
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = row_re.match(line)
            if m:
                code    = m.group(1)
                layer   = m.group(2).strip()
                concept = m.group(3).strip()
                if code not in nodes:
                    nodes[code] = {"code": code, "concept": concept,
                                   "layer": layer, "system": "BE"}
    return nodes


# ── 1.2  Parse VVV nodes ──────────────────────────────────────────────────────
def parse_vvv_nodes(path: Path) -> dict:
    """
    Parse N_QM_VVV_XXXXX nodes from node_QM_VVV.md table.
    Table columns: [1]=No  [2]=Node code  [3]=Node type  [4]=Concept  ...
    """
    nodes = {}
    row_re = re.compile(r'^\|\s*\d+\s*\|\s*(N_QM_VVV_\d{5})\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|')
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = row_re.match(line)
            if m:
                code      = m.group(1)
                node_type = m.group(2).strip()
                concept   = m.group(3).strip()
                if code not in nodes:
                    nodes[code] = {"code": code, "concept": concept,
                                   "layer": node_type, "system": "VVV"}
    return nodes


# ── 1.3  Parse QM nodes ───────────────────────────────────────────────────────
def parse_qm_nodes(path: Path) -> dict:
    """
    Parse N_QM_XXXXX nodes from system_qm_full.md table.
    Table columns: [1]=No  [2]=Node code  [3]=Layer  [4]=Concept  ...
    Skip N_QM_VVV codes that may appear in cross-refs.
    """
    nodes = {}
    row_re = re.compile(r'^\|\s*\d+\s*\|\s*(N_QM_\d{5})\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|')
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = row_re.match(line)
            if m:
                code    = m.group(1)
                layer   = m.group(2).strip()
                concept = m.group(3).strip()
                if code not in nodes:
                    nodes[code] = {"code": code, "concept": concept,
                                   "layer": layer, "system": "QM"}
    return nodes


# ── 1.4a  Parse VVV edges (115) ───────────────────────────────────────────────
def parse_vvv_edges(path: Path) -> list:
    """
    Parse ED_QM_VVV_XXXXX edges from edge_QM_VVV.md.
    Line format:  ED_QM_VVV_NNNNN: N_XXX_NNNNN (label) -> N_XXX_NNNNN (label)
    Followed by:  - **Relation:** rel_name -- description
    """
    edges = []
    # Use .*? to skip label (handles nested parens like "(ε(M))")
    edge_re     = re.compile(
        r'^(ED_QM_VVV_\d{5}):\s*(N_\w+)\b.*?[→>]\s*(N_\w+)\b'
    )
    relation_re = re.compile(r'^\s*-\s*\*\*Relation:\*\*\s*(\w[\w _/\-]*?)\s*[—\-]')
    pending = None
    with open(path, encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            m = edge_re.match(stripped)
            if m:
                src = m.group(2).strip()
                tgt = m.group(3).strip()
                if RE_VVV_CODE.match(src) and RE_VVV_CODE.match(tgt):
                    etype = "VVV_INTERNAL"
                elif RE_VVV_CODE.match(src) and RE_QM_CODE.match(tgt):
                    etype = "VVV_TO_QM"
                elif RE_VVV_CODE.match(src) and RE_BE_CODE.match(tgt):
                    etype = "VVV_TO_BE"
                else:
                    etype = "UNKNOWN"
                pending = {"edge_id": m.group(1), "source": src, "target": tgt,
                           "relation": "", "edge_type": etype}
            elif pending:
                mr = relation_re.match(stripped)
                if mr:
                    pending["relation"] = mr.group(1).strip()
                    edges.append(pending)
                    pending = None
    return edges


# ── 1.4b  Parse bridge edges (15) ────────────────────────────────────────────
def parse_bridge_edges(path: Path) -> tuple:
    """
    Parse BR_XXXXX bridge edges from bridge_QM_standard_to_VVV_QMRF.md table.
    Table: | `BR_XXXXX` | direction | qm_anchor_cell | vvv_anchor_cell | ...
    Returns (edges_list, skipped_list).
    """
    edges, skipped = [], []
    row_re = re.compile(r'^\|\s*`?(BR_\d{5})`?\s*\|([^|]*)\|([^|]*)\|([^|]*)\|')
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = row_re.match(line)
            if not m:
                continue
            bridge_id = m.group(1).strip()
            direction = m.group(2).strip()
            qm_cell   = m.group(3)
            vvv_cell  = m.group(4)

            qm_match  = RE_QM_CODE.search(qm_cell)
            vvv_match = RE_VVV_CODE.search(vvv_cell)

            if qm_match and vvv_match:
                qm_node  = qm_match.group(0)
                vvv_node = vvv_match.group(0)
                edges.append({
                    "edge_id":   bridge_id,
                    "source":    qm_node,
                    "target":    vvv_node,
                    "relation":  "bridge",
                    "direction": direction,
                    "edge_type": "BR_QM_VVV",
                    "status":    "checked",
                })
            else:
                skipped.append(f"{bridge_id} (boundary guard — no valid node codes)")
    return edges, skipped


# ── 1.4c  Parse draft bridge edges (19 rows / 21 links) ──────────────────────
def parse_draft_bridges(path: Path, bian_map: dict) -> tuple:
    """
    Parse 19 draft bridge rows from consolidated draft file.
    Table: | BR_DRAFT_X_NNN | batch | N_BE_XXXXX | be_status | BIAN-X[/Y] | ...
    Dual-target rows expand to 2 edges each.
    Returns (edges_list, warnings_list).
    """
    edges, warnings = [], []
    row_re = re.compile(
        r'^\|\s*(BR_DRAFT_\w+)\s*\|\s*([A-F])\s*\|\s*(N_BE_\d{5})\s*\|[^|]*\|\s*([^|]+?)\s*\|'
    )
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = row_re.match(line)
            if not m:
                continue
            draft_id   = m.group(1).strip()
            be_node    = m.group(3).strip()
            bian_field = m.group(4).strip()

            # Resolve BIAN targets — handle "BIAN-14/15" or "BIAN-15/9"
            bian_targets = []
            if "/" in bian_field:
                parts = bian_field.split("/")
                bian_targets.append(parts[0].strip())
                second = parts[1].strip()
                bian_targets.append(f"BIAN-{second}" if re.match(r'^\d+$', second) else second)
            else:
                bian_targets.append(bian_field)

            for idx, bian in enumerate(bian_targets):
                bian_key = bian.strip()
                vvv_node = bian_map.get(bian_key)
                if vvv_node:
                    eid = draft_id if idx == 0 else f"{draft_id}_b"
                    edges.append({
                        "edge_id":     eid,
                        "source":      be_node,
                        "target":      vvv_node,
                        "relation":    "draft_bridge_support",
                        "bian_target": bian_key,
                        "edge_type":   "DRAFT_BRIDGE_BE_VVV",
                        "status":      "draft",
                    })
                else:
                    warnings.append(f"{draft_id}: BIAN key '{bian_key}' not in BIAN_TO_VVV map")

    return edges, warnings


# ── 1.5  Build MultiDiGraph ──────────────────────────────────────────────────
def build_graph(be_nodes, vvv_nodes, qm_nodes, all_edges):
    G = nx.MultiDiGraph()
    G.graph["project"] = "VVV-QMRF-EX"
    G.graph["phase"]   = "1-graph-construction"
    G.graph["date"]    = "2026-05-20"

    for code, attrs in {**be_nodes, **vvv_nodes, **qm_nodes}.items():
        G.add_node(code, **attrs)

    for e in all_edges:
        e2  = dict(e)
        src = e2.pop("source")
        tgt = e2.pop("target")
        G.add_edge(src, tgt, **e2)

    return G


# ── 1.6  Validate ─────────────────────────────────────────────────────────────
def validate_graph(G, be_nodes, vvv_nodes, qm_nodes):
    node_set = set(G.nodes())
    dangling = []
    for u, v, data in G.edges(data=True):
        if u not in node_set or v not in node_set:
            dangling.append({"edge_id": data.get("edge_id", "?"), "source": u, "target": v})

    orphans = [n for n in G.nodes() if G.degree(n) == 0]

    be_count  = sum(1 for _, d in G.nodes(data=True) if d.get("system") == "BE")
    vvv_count = sum(1 for _, d in G.nodes(data=True) if d.get("system") == "VVV")
    qm_count  = sum(1 for _, d in G.nodes(data=True) if d.get("system") == "QM")

    edge_types: dict = {}
    for _, _, d in G.edges(data=True):
        et = d.get("edge_type", "UNKNOWN")
        edge_types[et] = edge_types.get(et, 0) + 1

    return {
        "total_nodes":      G.number_of_nodes(),
        "be_nodes":         be_count,
        "vvv_nodes":        vvv_count,
        "qm_nodes":         qm_count,
        "total_edges":      G.number_of_edges(),
        "edge_type_counts": edge_types,
        "dangling_edges":   dangling,
        "dangling_count":   len(dangling),
        "orphan_nodes":     orphans,
        "orphan_count":     len(orphans),
        "integrity_pass":   len(dangling) == 0,
    }


# ── Main ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 60)
    print("VVV-QMRF-EX  Phase 1 — Graph Construction")
    print("=" * 60)

    # Step 1.1
    be_nodes = parse_be_nodes(BE_SOT)
    print(f"\nStep 1.1  BE nodes:  {len(be_nodes):>4}  (expected 263)")

    # Step 1.2
    vvv_nodes = parse_vvv_nodes(VVV_NODES)
    print(f"Step 1.2  VVV nodes: {len(vvv_nodes):>4}  (expected 62)")

    # Step 1.3
    qm_nodes = parse_qm_nodes(QM_SOT)
    print(f"Step 1.3  QM nodes:  {len(qm_nodes):>4}  (expected 105)")

    # Step 1.4
    vvv_edges             = parse_vvv_edges(VVV_EDGES)
    bridge_edges, skipped = parse_bridge_edges(BRIDGE_FILE)
    draft_edges, warnings = parse_draft_bridges(DRAFT_FILE, BIAN_TO_VVV)

    p1 = sum(1 for e in vvv_edges if e["edge_type"] == "VVV_INTERNAL")
    p2 = sum(1 for e in vvv_edges if e["edge_type"] == "VVV_TO_QM")
    p3 = sum(1 for e in vvv_edges if e["edge_type"] == "VVV_TO_BE")
    print(f"\nStep 1.4  VVV edges:   {len(vvv_edges):>4}  "
          f"(P1={p1} P2={p2} P3={p3};  expected 131)")
    print(f"          BR bridges:  {len(bridge_edges):>4}  "
          f"(expected ~13 with node codes; {len(skipped)} boundary guards skipped)")
    print(f"          Draft links: {len(draft_edges):>4}  "
          f"(expected 21 = 19 rows + 2 dual-target expansions)")
    for s in skipped:
        print(f"  [SKIP] {s}")
    for w in warnings:
        print(f"  [WARN] {w}")

    # Step 1.5
    all_edges = vvv_edges + bridge_edges + draft_edges
    G = build_graph(be_nodes, vvv_nodes, qm_nodes, all_edges)
    print(f"\nStep 1.5  Graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

    # Step 1.6
    report = validate_graph(G, be_nodes, vvv_nodes, qm_nodes)
    print(f"\nStep 1.6  Validation:")
    print(f"  BE nodes:  {report['be_nodes']:>4}  (expected 263)")
    print(f"  VVV nodes: {report['vvv_nodes']:>4}  (expected 62)")
    print(f"  QM nodes:  {report['qm_nodes']:>4}  (expected 105)")
    print(f"  Total:     {report['total_nodes']}  (expected 430)")
    print(f"  Edges:     {report['total_edges']}  (expected ~165)")
    print(f"  Edge types: {report['edge_type_counts']}")
    print(f"  Dangling:  {report['dangling_count']}  (MUST be 0)")
    print(f"  Orphans:   {report['orphan_count']}  (permitted at Phase 1)")

    # Diagnostic: identify missing VVV edge IDs
    parsed_vvv_ids = {e["edge_id"] for e in vvv_edges}
    missing_p2 = sorted({f"ED_QM_VVV_{i:05d}" for i in range(41, 101)} - parsed_vvv_ids)
    if missing_p2:
        print(f"  [DIAG] Missing Phase 2 edges: {missing_p2}")

    if not report["integrity_pass"]:
        print("\n[FAIL] BLOCKING -- dangling edge refs found. STOP before Phase 2.")
        for d in report["dangling_edges"]:
            print(f"    {d['edge_id']}: {d['source']} -> {d['target']}")
        sys.exit(1)

    print("  [OK] Zero dangling edge references")

    # Save graph JSON
    OUT.mkdir(parents=True, exist_ok=True)
    graph_path = OUT / "vvv_qmrf_ex_graph.json"
    data = json_graph.node_link_data(G)
    with open(graph_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"\n[OK] Graph saved:       {graph_path}")

    # Save validation report
    report_path = OUT / f"phase1_validation_report{SUFFIX}.json"
    saveable = {k: v for k, v in report.items()
                if k not in ("dangling_edges", "orphan_nodes")}
    saveable["dangling_sample"]           = report["dangling_edges"][:5]
    saveable["orphan_sample"]             = report["orphan_nodes"][:30]
    saveable["boundary_guards_skipped"]   = skipped
    saveable["draft_bridge_warnings"]     = warnings
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(saveable, f, ensure_ascii=False, indent=2)
    print(f"[OK] Validation report: {report_path}")

    print("\n" + "=" * 60)
    print("Phase 1 COMPLETE — ready for Phase 2 (Intersection Analysis)")
    print("=" * 60)
