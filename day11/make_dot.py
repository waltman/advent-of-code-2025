import sys
import networkx as nx

outputs = dict()
with open(sys.argv[1]) as f:
    for line in f:
        device = line[0:3]
        outs = [tok for tok in line[5:].rstrip().split(' ')]
        outputs[device] = outs

print('digraph G {')
for k,v in outputs.items():
    for node in v:
        print(f'  {k} -> {node}')
print('}')

