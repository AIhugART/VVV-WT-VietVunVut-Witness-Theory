"""
VVV-QMRF-EX Phase 2 — Intersection Analysis
Plan: vvv-qmrf-ex-plan.md §7 Phase 2 (Steps 2.1-2.6)
Execution: C:/Users/PC/AppData/Local/Programs/Python/Python312/python.exe

Steps:
  2.1 Compute intersection nodes (VVV with K-side BE + rho-side QM anchoring)
  2.2 Compute betweenness centrality -> vvv_qmrf_ex_centrality.csv
  2.3 Detect community structure (greedy modularity, undirected)
  2.4 Sample shortest paths BE->QM through VVV layer
  2.5 Identify K-side gaps (VVV without BE anchoring)
  2.6 Identify rho-side gaps (VVV without QM anchoring)

Outputs (all in vvv-qmrf-ex/):
  data/vvv_qmrf_ex_centrality.csv
  data/phase2_intersection_report.json
  vvv_qmrf_ex_intersection.md  (Phase 2 preliminary)
  vvv_qmrf_ex_gaps.md          (Phase 2 preliminary)

Edge type definitions from Phase 1:
  VVV_INTERNAL         : VVV <-> VVV  (40 edges)
  VVV_TO_QM            : VVV  -> QM   (60 edges)  rho-side
  VVV_TO_BE            : VVV  -> BE   (15 edges)  K-side
  BR_QM_VVV            : QM   -> VVV  (13 edges)  rho-side (reverse bridge)
  DRAFT_BRIDGE_BE_VVV  : BE   -> VVV  (21 edges)  K-side (draft)
"""

import csv
import json
import os
import sys
from pathlib import Path

import networkx as nx
from networkx.readwrite import json_graph

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SUFFIX = os.environ.get("VVV_QMRF_EX_SUFFIX", "")

# ── Paths ─────────────────────────────────────────────────────────────────────
BASE = Path("c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement")
OUT  = BASE / "documents/research_documents/vvv-qmrf-ex"
DATA = OUT / "data"

GRAPH_JSON = DATA / "vvv_qmrf_ex_graph.json"

AUTHOR = (
    "Author: VietVunVut (Viet - Nguyen Xuan); "
    "GitHub: https://github.com/AIhugART/; "
    "Facebook: https://www.facebook.com/xuanviet"
)

K_SIDE_TYPES   = {"VVV_TO_BE", "DRAFT_BRIDGE_BE_VVV", "BR_EX_BE", "BR_EX_BE_NEW", "BR_EX_BE_STRETCH"}
RHO_SIDE_TYPES = {"VVV_TO_QM", "BR_QM_VVV", "BR_EX_QM", "BR_EX_QM_NEW"}


# ── Graph loading ─────────────────────────────────────────────────────────────
def load_graph(path: Path) -> nx.MultiDiGraph:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    try:
        return json_graph.node_link_graph(data, edges="edges")
    except TypeError:
        # Older networkx: rename 'edges' to 'links' manually
        if 'edges' in data and 'links' not in data:
            data['links'] = data.pop('edges')
        return json_graph.node_link_graph(data)


# ── Node layer helpers ────────────────────────────────────────────────────────
def layer_nodes(G, system: str):
    return [n for n, d in G.nodes(data=True) if d.get("system") == system]


# ── 2.1  Intersection + gap detection ────────────────────────────────────────
def compute_intersection(G):
    """
    For each VVV node:
      K-side  : touches BE via VVV_TO_BE (outgoing) or DRAFT_BRIDGE_BE_VVV (incoming)
      rho-side: touches QM via VVV_TO_QM (outgoing) or BR_QM_VVV (incoming)
    Returns dict {node: {"k_side_be": [...], "rho_side_qm": [...], "in_intersection": bool}}
    """
    result = {}
    for node in layer_nodes(G, "VVV"):
        k_be_neighbors   = set()
        rho_qm_neighbors = set()

        for u, v, data in G.out_edges(node, data=True):
            et = data.get("edge_type", "")
            if et in K_SIDE_TYPES   and G.nodes[v].get("system") == "BE":
                k_be_neighbors.add(v)
            if et in RHO_SIDE_TYPES and G.nodes[v].get("system") == "QM":
                rho_qm_neighbors.add(v)

        for u, v, data in G.in_edges(node, data=True):
            et = data.get("edge_type", "")
            if et in K_SIDE_TYPES   and G.nodes[u].get("system") == "BE":
                k_be_neighbors.add(u)
            if et in RHO_SIDE_TYPES and G.nodes[u].get("system") == "QM":
                rho_qm_neighbors.add(u)

        result[node] = {
            "k_side_be":       sorted(k_be_neighbors),
            "rho_side_qm":     sorted(rho_qm_neighbors),
            "in_intersection": bool(k_be_neighbors) and bool(rho_qm_neighbors),
        }
    return result


# ── 2.2  Betweenness centrality ───────────────────────────────────────────────
def compute_centrality(G: nx.MultiDiGraph):
    """
    Collapse MultiDiGraph to DiGraph (parallel edges -> weight sum),
    then compute normalized betweenness centrality.
    """
    G_simple = nx.DiGraph()
    for n, d in G.nodes(data=True):
        G_simple.add_node(n, **d)
    for u, v, data in G.edges(data=True):
        if G_simple.has_edge(u, v):
            G_simple[u][v]["weight"] += 1
        else:
            G_simple.add_edge(u, v, weight=1)
    return nx.betweenness_centrality(G_simple, normalized=True)


# ── 2.3  Community detection ──────────────────────────────────────────────────
def detect_communities(G: nx.MultiDiGraph):
    """
    Greedy modularity communities on undirected simple projection.
    NetworkX 3.3 exposes no random_state parameter for this function, so
    output ordering is stabilized after detection for reproducible reports.
    """
    G_simple = nx.Graph(G.to_undirected())
    communities = nx.community.greedy_modularity_communities(G_simple)
    return sorted(communities, key=lambda c: (-len(c), sorted(c)))


# ── 2.4  Sample shortest paths BE -> QM ──────────────────────────────────────
def compute_shortest_paths(G: nx.MultiDiGraph, limit: int = 30):
    """
    Enumerate shortest paths from BE nodes (with out-edges) to reachable QM
    nodes. Retain only paths that pass through at least one VVV node.
    """
    be_with_edges = [n for n in layer_nodes(G, "BE") if G.out_degree(n) > 0]
    qm_with_edges = [n for n in layer_nodes(G, "QM") if G.in_degree(n) > 0]

    paths = []
    for be_n in be_with_edges:
        for qm_n in qm_with_edges:
            try:
                path = nx.shortest_path(G, be_n, qm_n)
            except (nx.NetworkXNoPath, nx.NodeNotFound):
                continue
            vvv_hops = [p for p in path[1:-1] if G.nodes[p].get("system") == "VVV"]
            if vvv_hops:
                paths.append({
                    "source":   be_n,
                    "target":   qm_n,
                    "path":     path,
                    "length":   len(path) - 1,
                    "vvv_hops": vvv_hops,
                })
                if len(paths) >= limit:
                    return paths
    return paths


# ── Markdown helpers ──────────────────────────────────────────────────────────
def concept(G, node_id):
    return G.nodes[node_id].get("concept", node_id)


def write_intersection_md(G, intersection, bc, communities, paths, report, path: Path):
    vvv_total   = report["vvv_total"]
    inter_ct    = report["intersection_count"]
    k_gap_ct    = len(report["k_gaps"])
    rho_gap_ct  = len(report["rho_gaps"])
    both_ct     = len(report["both_gaps"])
    only_k_ct   = k_gap_ct - both_ct
    only_rho_ct = rho_gap_ct - both_ct

    lines = [
        AUTHOR,
        "",
        "# VVV-QMRF-EX — Intersection Analysis",
        "> **Phase:** 2 preliminary — will be enriched in Phase 4 after similarity search",
        "> **Date:** 2026-05-20",
        "> **Source graph:** `data/vvv_qmrf_ex_graph.json`",
        "> **Full data:** `data/phase2_intersection_report.json`",
        "",
        "---",
        "",
        "## 1. K-rho Intersection Nodes",
        "",
        "> VVV node is in intersection if it has >= 1 K-side BE anchor (via `VVV_TO_BE` or "
        "`DRAFT_BRIDGE_BE_VVV`) AND >= 1 rho-side QM anchor (via `VVV_TO_QM` or `BR_QM_VVV`).",
        "",
        f"**Count:** {inter_ct} / {vvv_total} VVV nodes ({inter_ct / vvv_total * 100:.1f}%)",
        "",
        "| VVV Node | Concept | K-side BE anchors | rho-side QM anchors |",
        "|---|---|---|---|",
    ]
    for n in sorted(intersection.keys()):
        d = intersection[n]
        if not d["in_intersection"]:
            continue
        k_list   = ", ".join(
            f"`{x}` ({concept(G, x)[:30]})" for x in d["k_side_be"]
        )
        rho_list = ", ".join(
            f"`{x}` ({concept(G, x)[:30]})" for x in d["rho_side_qm"]
        )
        lines.append(
            f"| `{n}` | {concept(G, n)[:45]} | {k_list} | {rho_list} |"
        )

    lines += [
        "",
        "---",
        "",
        "## 2. Betweenness Centrality — Top VVV Mediators",
        "",
        "| Rank | VVV Node | Concept | Betweenness | In Intersection |",
        "|---|---|---|---|---|",
    ]
    for rank, item in enumerate(report["top_vvv_mediators"], 1):
        n      = item["node"]
        in_int = "Yes" if intersection[n]["in_intersection"] else "No"
        lines.append(
            f"| {rank} | `{n}` | {item['concept'][:45]} | "
            f"{item['betweenness']:.6f} | {in_int} |"
        )

    lines += [
        "",
        "---",
        "",
        "## 3. Community Structure",
        "",
        f"Greedy modularity communities: **{report['community_count']}**",
        "",
        "| Community | Size | BE | VVV | QM | VVV members |",
        "|---|---|---|---|---|---|",
    ]
    for c in report["community_summary"]:
        vvv_str = ", ".join(f"`{x}`" for x in c["vvv_members"][:6])
        if len(c["vvv_members"]) > 6:
            vvv_str += f" +{len(c['vvv_members']) - 6} more"
        lines.append(
            f"| {c['id']} | {c['size']} | {c['be_nodes']} | "
            f"{c['vvv_nodes']} | {c['qm_nodes']} | {vvv_str} |"
        )

    lines += [
        "",
        "---",
        "",
        "## 4. Sample Shortest Paths BE -> VVV -> QM",
        "",
        f"Paths found (shown <= 20, limit=30): **{len(report['sample_paths_be_to_qm'])}**",
        f"Direct BE->QM edges (must be 0): **{report['direct_be_qm_edges']}**",
        "",
        "| Source (BE) | Via VVV | Target (QM) | Length |",
        "|---|---|---|---|",
    ]
    for p in report["sample_paths_be_to_qm"][:20]:
        via = ", ".join(f"`{v}`" for v in p["vvv_hops"])
        lines.append(
            f"| `{p['source']}` ({concept(G, p['source'])[:28]}) "
            f"| {via} "
            f"| `{p['target']}` ({concept(G, p['target'])[:28]}) "
            f"| {p['length']} |"
        )

    lines += [
        "",
        "---",
        "",
        "## 5. Coverage Summary",
        "",
        "| Category | Count | % of 52 VVV |",
        "|---|---|---|",
        f"| Intersection (dual K-rho anchored) | {inter_ct} | {inter_ct/vvv_total*100:.1f}% |",
        f"| K-side gap only (no BE, has QM) | {only_k_ct} | {only_k_ct/vvv_total*100:.1f}% |",
        f"| rho-side gap only (has BE, no QM) | {only_rho_ct} | {only_rho_ct/vvv_total*100:.1f}% |",
        f"| Both gaps (no BE and no QM) | {both_ct} | {both_ct/vvv_total*100:.1f}% |",
        "",
        "> Intersection nodes are Phase 4 registry targets (formalize as BR_EX edges).",
        "> Gap nodes are Phase 4 expansion targets.",
        "",
        "---",
        "",
        "## 6. Integrity Checks",
        "",
        "| Check | Result |",
        "|---|---|",
        f"| Intersection >= 15 nodes | "
        f"{'[OK]' if report['integrity_checks']['intersection_ge_15'] else '[FAIL]'} "
        f"({inter_ct} nodes) |",
        f"| No direct BE->QM edges | "
        f"{'[OK]' if report['integrity_checks']['no_direct_be_qm'] else '[FAIL]'} "
        f"(count = {report['direct_be_qm_edges']}) |",
        "",
        "---",
        "",
        "© 2026 VietVunVut (Viet - Nguyen Xuan). Licensed under CC BY 4.0.",
        "To view a copy of this license, visit https://creativecommons.org/licenses/by/4.0/",
    ]

    path.write_text("\n".join(lines), encoding="utf-8")


def write_gaps_md(G, intersection, report, path: Path):
    k_gaps  = report["k_gaps"]
    rho_gaps = report["rho_gaps"]
    both    = set(report["both_gaps"])

    lines = [
        AUTHOR,
        "",
        "# VVV-QMRF-EX — Gap Analysis",
        "> **Phase:** 2 preliminary — Phase 3 similarity search will enrich gap classification.",
        "> **Date:** 2026-05-20",
        "",
        "---",
        "",
        "## 1. K-side Gaps — VVV nodes without BE anchoring",
        "",
        "> No `VVV_TO_BE` (outgoing) or `DRAFT_BRIDGE_BE_VVV` (incoming) edges.",
        "> **Bridge 1 expansion targets** for Phase 4.",
        "",
        f"**Count:** {len(k_gaps)} nodes",
        "",
        "| VVV Node | Concept | Also rho-gap? | rho-side QM anchors |",
        "|---|---|---|---|",
    ]
    for n in sorted(k_gaps.keys()):
        also_rho = "Yes" if n in rho_gaps else "No"
        rho_list = ", ".join(f"`{x}`" for x in intersection[n]["rho_side_qm"]) or "—"
        lines.append(f"| `{n}` | {k_gaps[n][:50]} | {also_rho} | {rho_list} |")

    lines += [
        "",
        "---",
        "",
        "## 2. rho-side Gaps — VVV nodes without QM anchoring",
        "",
        "> No `VVV_TO_QM` (outgoing) or `BR_QM_VVV` (incoming) edges.",
        "> **Bridge 2 expansion targets** for Phase 4.",
        "",
        f"**Count:** {len(rho_gaps)} nodes",
        "",
        "| VVV Node | Concept | Also K-gap? | K-side BE anchors |",
        "|---|---|---|---|",
    ]
    for n in sorted(rho_gaps.keys()):
        also_k = "Yes" if n in k_gaps else "No"
        k_list = ", ".join(f"`{x}`" for x in intersection[n]["k_side_be"]) or "—"
        lines.append(f"| `{n}` | {rho_gaps[n][:50]} | {also_k} | {k_list} |")

    lines += [
        "",
        "---",
        "",
        "## 3. Both-Gap Nodes (no BE and no QM anchor)",
        "",
        "> Pure VVV-internal nodes. Phase 3 similarity search may reveal latent connections.",
        "",
        f"**Count:** {len(both)} nodes",
        "",
        "| VVV Node | Concept |",
        "|---|---|",
    ]
    for n in sorted(both):
        lines.append(f"| `{n}` | {G.nodes[n].get('concept', '')[:60]} |")

    lines += [
        "",
        "---",
        "",
        "## 4. Summary",
        "",
        "| Category | Count |",
        "|---|---|",
        f"| K-side gaps (no BE anchor) | {len(k_gaps)} |",
        f"| rho-side gaps (no QM anchor) | {len(rho_gaps)} |",
        f"| Both gaps (no BE and no QM) | {len(both)} |",
        f"| Intersection (both anchored) | {report['intersection_count']} |",
        f"| **Total VVV nodes** | **{report['vvv_total']}** |",
        "",
        "> Phase 3 similarity search will produce similarity-scored gap candidates.",
        "> Phase 4 bridge registry will formalize BR_EX_BE / BR_EX_QM for gap nodes.",
        "",
        "---",
        "",
        "© 2026 VietVunVut (Viet - Nguyen Xuan). Licensed under CC BY 4.0.",
        "To view a copy of this license, visit https://creativecommons.org/licenses/by/4.0/",
    ]

    path.write_text("\n".join(lines), encoding="utf-8")


# ── Main ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 60)
    print("VVV-QMRF-EX  Phase 2 -- Intersection Analysis")
    print("=" * 60)

    G = load_graph(GRAPH_JSON)
    all_vvv = layer_nodes(G, "VVV")
    all_be  = layer_nodes(G, "BE")
    all_qm  = layer_nodes(G, "QM")
    print(f"\nGraph: {G.number_of_nodes()} nodes "
          f"({len(all_be)} BE, {len(all_vvv)} VVV, {len(all_qm)} QM), "
          f"{G.number_of_edges()} edges")

    # 2.1
    print("\nStep 2.1  Intersection + gap detection...")
    intersection = compute_intersection(G)
    intersect_list = sorted(n for n, v in intersection.items() if v["in_intersection"])
    k_gaps   = {n: G.nodes[n].get("concept", "")
                for n, v in intersection.items() if not v["k_side_be"]}
    rho_gaps = {n: G.nodes[n].get("concept", "")
                for n, v in intersection.items() if not v["rho_side_qm"]}
    both_gaps = sorted(set(k_gaps) & set(rho_gaps))
    print(f"  Intersection (dual K-rho):  {len(intersect_list)}")
    print(f"  K-side gaps (no BE anchor): {len(k_gaps)}")
    print(f"  rho-side gaps (no QM):      {len(rho_gaps)}")
    print(f"  Both gaps (no BE + no QM):  {len(both_gaps)}")
    if len(intersect_list) >= 15:
        print(f"  [OK] >= 15 intersection nodes")
    else:
        print(f"  [WARN] Only {len(intersect_list)} intersection nodes (expected >= 15)")

    # 2.2
    print("\nStep 2.2  Betweenness centrality...")
    bc = compute_centrality(G)
    vvv_bc = sorted(
        [(n, bc.get(n, 0.0)) for n in all_vvv],
        key=lambda x: x[1], reverse=True
    )
    print("  Top 5 VVV mediators:")
    for n, score in vvv_bc[:5]:
        print(f"    {n}  {score:.6f}  {G.nodes[n].get('concept', '')[:45]}")

    centrality_path = DATA / "vvv_qmrf_ex_centrality.csv"
    with open(centrality_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["node_id", "system", "concept", "betweenness_centrality"])
        for n, score in sorted(bc.items(), key=lambda x: x[1], reverse=True):
            d = G.nodes[n]
            w.writerow([n, d.get("system", "?"), d.get("concept", "?")[:80], f"{score:.8f}"])
    print(f"  Saved: {centrality_path}")

    # 2.3
    print("\nStep 2.3  Community detection (greedy modularity)...")
    communities = detect_communities(G)
    print(f"  Communities: {len(communities)}")
    community_summary = []
    for i, c in enumerate(communities):
        be_c  = sum(1 for n in c if G.nodes[n].get("system") == "BE")
        vvv_c = sum(1 for n in c if G.nodes[n].get("system") == "VVV")
        qm_c  = sum(1 for n in c if G.nodes[n].get("system") == "QM")
        vvv_m = sorted(n for n in c if G.nodes[n].get("system") == "VVV")
        community_summary.append({
            "id": i + 1, "size": len(c),
            "be_nodes": be_c, "vvv_nodes": vvv_c, "qm_nodes": qm_c,
            "vvv_members": vvv_m,
        })
        if i < 6:
            print(f"  Community {i+1}: {len(c)} nodes "
                  f"(BE={be_c}, VVV={vvv_c}, QM={qm_c})")
    if len(communities) > 6:
        print(f"  ... ({len(communities) - 6} more)")

    # 2.4
    print("\nStep 2.4  Shortest paths BE->QM...")
    paths = compute_shortest_paths(G, limit=30)
    direct_be_qm = sum(
        1 for be_n in all_be for qm_n in all_qm if G.has_edge(be_n, qm_n)
    )
    print(f"  Paths through VVV found: {len(paths)}")
    print(f"  Direct BE->QM edges:     {direct_be_qm}  (expected 0)")
    if direct_be_qm == 0:
        print("  [OK] No direct BE->QM edges")
    else:
        print(f"  [WARN] {direct_be_qm} direct BE->QM edges found")

    # 2.5 / 2.6
    print(f"\nStep 2.5  K-side gaps: {len(k_gaps)}")
    print(f"Step 2.6  rho-side gaps: {len(rho_gaps)}")

    # Build report
    report = {
        "phase": "2-intersection-analysis",
        "date": "2026-05-20",
        "graph_nodes": G.number_of_nodes(),
        "graph_edges": G.number_of_edges(),
        "vvv_total": len(all_vvv),
        "intersection_count": len(intersect_list),
        "intersection_nodes": {
            n: {
                "concept":    G.nodes[n].get("concept", ""),
                "k_side_be":  intersection[n]["k_side_be"],
                "rho_side_qm": intersection[n]["rho_side_qm"],
            }
            for n in intersect_list
        },
        "k_gaps":    k_gaps,
        "rho_gaps":  rho_gaps,
        "both_gaps": both_gaps,
        "top_vvv_mediators": [
            {
                "node":            n,
                "concept":         G.nodes[n].get("concept", ""),
                "betweenness":     round(score, 8),
                "in_intersection": intersection[n]["in_intersection"],
            }
            for n, score in vvv_bc[:15]
        ],
        "community_count":   len(communities),
        "community_summary": community_summary,
        "sample_paths_be_to_qm": paths[:20],
        "direct_be_qm_edges": direct_be_qm,
        "integrity_checks": {
            "intersection_ge_15": len(intersect_list) >= 15,
            "no_direct_be_qm":    direct_be_qm == 0,
        },
    }

    report_path = DATA / f"phase2_intersection_report{SUFFIX}.json"
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"\nSaved: {report_path}")

    # Markdown outputs
    print("\nGenerating markdown...")
    intersection_md = OUT / "vvv_qmrf_ex_intersection.md"
    gaps_md         = OUT / "vvv_qmrf_ex_gaps.md"

    write_intersection_md(G, intersection, bc, communities, paths, report, intersection_md)
    print(f"  Saved: {intersection_md}")

    write_gaps_md(G, intersection, report, gaps_md)
    print(f"  Saved: {gaps_md}")

    # Summary
    all_pass = (report["integrity_checks"]["intersection_ge_15"]
                and report["integrity_checks"]["no_direct_be_qm"])
    print("\n" + "=" * 60)
    print("Phase 2 complete.")
    print(f"  Intersection:   {len(intersect_list)} / {len(all_vvv)} VVV nodes")
    print(f"  K-side gaps:    {len(k_gaps)}")
    print(f"  rho-side gaps:  {len(rho_gaps)}")
    print(f"  Both gaps:      {len(both_gaps)}")
    print(f"  Communities:    {len(communities)}")
    print(f"  Paths BE->QM:   {len(paths)}")
    print(f"  Integrity:      {'[OK] All checks pass' if all_pass else '[FAIL] See report'}")
    print("=" * 60)
