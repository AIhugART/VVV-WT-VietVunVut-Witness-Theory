import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Stable_Diffusion\Buddhist_Epistemology_Quantum_Measurement\documents\research_documents\mapping\Buddhist_Epistemology_and_Quantum_Measurement_system_mapping_SOT.md','r',encoding='utf-8') as f:
    text = f.read()

# Extract all edges
edges = re.findall(r'ED_BE_\d+:\s*(N_BE_\d+)\s*(?:\([^)]*\))?\s*(?:→|->)\s*(N_BE_\d+)', text)
print(f'Total edges found: {len(edges)}')

# Build adjacency
adj = {}
for src, tgt in edges:
    adj.setdefault(src, set()).add(tgt)
    
# Find all nodes
all_nodes = set()
for src, tgt in edges:
    all_nodes.add(src)
    all_nodes.add(tgt)
print(f'Total unique nodes: {len(all_nodes)}')

# BFS
def bfs(start, adj_map):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node in visited:
            continue
        visited.add(node)
        for nb in adj_map.get(node, []):
            if nb not in visited:
                queue.append(nb)
    return visited

# Check undirected connectivity
undirected_adj = {}
for src, tgt in edges:
    undirected_adj.setdefault(src, set()).add(tgt)
    undirected_adj.setdefault(tgt, set()).add(src)

start_node = sorted(all_nodes)[0]
reachable = bfs(start_node, undirected_adj)
unreachable = all_nodes - reachable
print(f'Reachable from {start_node} (undirected): {len(reachable)}/{len(all_nodes)}')
if unreachable:
    print(f'Unreachable nodes: {sorted(unreachable)}')
else:
    print('ALL NODES CONNECTED — graph is connected (undirected)')

# Key nodes
key_nodes = {
    'N_BE_00001': 'Pramana',
    'N_BE_00002': 'Pratyaksa', 
    'N_BE_00003': 'Anumana',
    'N_BE_00005': 'Prameya',
    'N_BE_00011': 'Svasamvedana',
    'N_BE_00013': 'Svalaksana',
    'N_BE_00014': 'Samanyalaksana',
    'N_BE_00015': 'Apoha',
    'N_BE_00016': 'Linga',
    'N_BE_00018': 'Trairupya',
    'N_BE_00019': 'Vyapti',
    'N_BE_00021': 'Svabhavapratibandha',
    'N_BE_00022': 'Arthakriya',
    'N_BE_00025': 'Pramana-phala',
    'N_BE_00029': 'Ksanikavada',
}

print('\n=== KEY DEPENDENCY CHAINS ===')
for node in sorted(key_nodes.keys()):
    name = key_nodes[node]
    outgoing = adj.get(node, set())
    incoming = set()
    for src, targets in adj.items():
        if node in targets:
            incoming.add(src)
    
    out_named = []
    for n in sorted(outgoing):
        label = key_nodes.get(n, n)
        out_named.append(label)
    
    in_named = []
    for n in sorted(incoming):
        label = key_nodes.get(n, n)
        in_named.append(label)
    
    print(f'\n{node} ({name}):')
    print(f'  SENDS TO ({len(outgoing)}): {", ".join(out_named[:8])}')
    print(f'  RECEIVES ({len(incoming)}): {", ".join(in_named[:8])}')

# Find circular dependencies (directed cycles)
print('\n=== CIRCULAR DEPENDENCIES ===')
# Check specific chains
chains_to_test = [
    ['N_BE_00001', 'N_BE_00002', 'N_BE_00013', 'N_BE_00022'],
    ['N_BE_00001', 'N_BE_00003', 'N_BE_00018', 'N_BE_00019', 'N_BE_00021', 'N_BE_00022'],
    ['N_BE_00001', 'N_BE_00011'],
    ['N_BE_00002', 'N_BE_00013', 'N_BE_00022'],
]

for chain in chains_to_test:
    names = [key_nodes.get(n, n) for n in chain]
    valid = True
    for i in range(len(chain)-1):
        if chain[i+1] not in adj.get(chain[i], set()):
            valid = False
            break
    # Check if last can reach first
    can_return = chain[0] in bfs(chain[-1], adj)
    status = "CYCLE" if valid and can_return else ("CHAIN" if valid else "BROKEN")
    print(f'  {" -> ".join(names)}: {status}')

# Count mutual dependencies
print('\n=== MUTUAL DEPENDENCIES (A->B and B->A exist) ===')
mutual = 0
for src in adj:
    for tgt in adj[src]:
        if src in adj.get(tgt, set()):
            s_name = key_nodes.get(src, src)
            t_name = key_nodes.get(tgt, tgt)
            if src < tgt:  # avoid duplicates
                print(f'  {s_name} <-> {t_name}')
                mutual += 1
print(f'Total mutual dependency pairs: {mutual}')
