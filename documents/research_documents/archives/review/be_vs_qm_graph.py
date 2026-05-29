import re, sys
sys.stdout.reconfigure(encoding='utf-8')

def analyze_graph(filepath, edge_pattern):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    edges = re.findall(edge_pattern, text)
    adj = {}
    all_nodes = set()
    out_c = {}
    in_c = {}
    for src, tgt in edges:
        all_nodes.add(src); all_nodes.add(tgt)
        adj.setdefault(src, set()).add(tgt)
        out_c[src] = out_c.get(src, 0) + 1
        in_c[tgt] = in_c.get(tgt, 0) + 1
    
    # BFS undirected
    und = {}
    for s, t in edges:
        und.setdefault(s, set()).add(t)
        und.setdefault(t, set()).add(s)
    visited = set()
    queue = [sorted(all_nodes)[0]]
    while queue:
        n = queue.pop(0)
        if n in visited: continue
        visited.add(n)
        for nb in und.get(n, []):
            if nb not in visited: queue.append(nb)
    
    # Count components
    remaining = all_nodes - visited
    components = 1
    while remaining:
        components += 1
        queue = [sorted(remaining)[0]]
        while queue:
            n = queue.pop(0)
            if n not in remaining: continue
            remaining.discard(n)
            for nb in und.get(n, []):
                if nb in remaining: queue.append(nb)
    
    isolated = [n for n in all_nodes if out_c.get(n,0) + in_c.get(n,0) == 0]
    sink = [n for n in all_nodes if out_c.get(n,0) == 0 and in_c.get(n,0) > 0]
    source = [n for n in all_nodes if in_c.get(n,0) == 0 and out_c.get(n,0) > 0]
    
    edge_counts = [out_c.get(n,0) + in_c.get(n,0) for n in all_nodes]
    
    return {
        'nodes': len(all_nodes),
        'edges': len(set(edges)),
        'components': components,
        'connected': len(visited),
        'isolated': len(isolated),
        'sinks': len(sink),
        'sources': len(source),
        'avg_degree': sum(edge_counts)/len(edge_counts) if edge_counts else 0,
        'max_degree': max(edge_counts) if edge_counts else 0,
        'density': len(set(edges)) / (len(all_nodes) * (len(all_nodes)-1)) if len(all_nodes) > 1 else 0,
    }

# BE
be = analyze_graph(
    r'c:\Stable_Diffusion\Buddhist_Epistemology_Quantum_Measurement\documents\research_documents\mapping\Buddhist_Epistemology_and_Quantum_Measurement_system_mapping_SOT.md',
    r'ED_BE_\d+:\s*(N_BE_\d+)\s*(?:\([^)]*\))?\s*(?:->|→)\s*(N_BE_\d+)'
)

# QM
qm = analyze_graph(
    r'c:\Stable_Diffusion\Buddhist_Epistemology_Quantum_Measurement\documents\published_documents\edge_pub_doc_QM_Measurement.md',
    r'ED_QM_\d+:\s*(N_QM_\d+)\s*(?:\([^)]*\))?\s*(?:->|→)\s*(N_QM_\d+)'
)

print(f'{"Metric":<25} {"BE":>10} {"QM":>10}')
print('-' * 47)
for key in ['nodes', 'edges', 'components', 'isolated', 'sinks', 'sources']:
    print(f'{key:<25} {be[key]:>10} {qm[key]:>10}')
print(f'{"avg_degree":<25} {be["avg_degree"]:>10.1f} {qm["avg_degree"]:>10.1f}')
print(f'{"max_degree":<25} {be["max_degree"]:>10} {qm["max_degree"]:>10}')
print(f'{"density":<25} {be["density"]:>10.4f} {qm["density"]:>10.4f}')
print(f'{"edges/node ratio":<25} {be["edges"]/be["nodes"]:>10.2f} {qm["edges"]/qm["nodes"]:>10.2f}')
print(f'\n{"connected (undirected)":<25} {be["connected"]}/{be["nodes"]:>3} {qm["connected"]}/{qm["nodes"]:>3}')
