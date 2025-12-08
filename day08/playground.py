import sys
from itertools import combinations
import networkx as nx
from math import prod

def dist(b1, b2):
    return sum([(b1[0]-b2[0])**2, (b1[1]-b2[1])**2, (b1[2]-b2[2])**2])

def main():
    fname = sys.argv[1]
    num_juncs = int(sys.argv[2])
    with open(fname) as f:
        boxes = []
        for line in f:
            p1,p2,p3 = [int(n) for n in line.split(',')]
            boxes.append((p1,p2,p3))
                        

    G = nx.Graph()
    G.add_nodes_from(boxes)
        
    dists = {(b1,b2): dist(b1, b2) for b1, b2 in combinations(boxes, 2)}

    sorted_juncs = [item[0] for item in sorted(dists.items(), key=lambda item: item[1])]
    for box_pair in sorted_juncs[:num_juncs]:
        b1, b2 = box_pair
        G.add_edge(b1, b2)

    print('Part 1:', prod([len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)][0:3]))
    
    i = num_juncs
    while nx.number_connected_components(G) > 1:
        b1, b2 = sorted_juncs[i]
        G.add_edge(b1, b2)
        i += 1

    print('Part 2:', b1[0] * b2[0])

main()
