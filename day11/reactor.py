import sys
import networkx as nx

outputs = dict()
with open(sys.argv[1]) as f:
    for line in f:
        device = line[0:3]
        outs = [tok for tok in line[5:].rstrip().split(' ')]
        outputs[device] = outs

DG = nx.DiGraph()
for k,v in outputs.items():
    for node in v:
        DG.add_edge(k, node)

part1 = 0
stack = ['you']
while stack:
    if (node := stack.pop()) == 'out':
        part1 += 1
    else:
        stack += DG.neighbors(node)

print('Part 1:', part1)

