import sys
from math import sqrt
from itertools import combinations
import networkx as nx

def dist(b1, b2):
    return sqrt(sum([(b1[0]-b2[0])**2, (b1[1]-b2[1])**2, (b1[2]-b2[2])**2]))

def main():
    fname = sys.argv[1]
    num_juncs = int(sys.argv[2])
    with open(fname) as f:
        boxes = []
        for line in f:
            p1,p2,p3 = [int(n) for n in line.split(',')]
            boxes.append((p1,p2,p3))
                        

    print(boxes)
    G = nx.Graph(boxes)
    # for box in boxes:
    #     print(box)
    #     G.add_node(box)
        
    dists = {(b1,b2): dist(b1, b2) for b1, b2 in combinations(boxes, 2)}

    js = [item[0] for item in sorted(dists.items(), key=lambda item: item[1])][:num_juncs]
    for box_pair in js:
        b1, b2 = box_pair
        G.add_edge(b1, b2)

    print(f'G has {nx.number_connected_components(G)} connected components')

main()
