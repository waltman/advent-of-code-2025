import sys
from math import sqrt
from itertools import combinations
import networkx as nx

def dist(b1, b2):
    return sqrt(sum([(b1[0]-b2[0])**2, (b1[1]-b2[1])**2, (b1[2]-b2[2])**2]))

def main():
    with open(sys.argv[1]) as f:
        boxes = [[int(tok) for tok in line.rstrip().split(',')] for line in f]

    min_dist = 1e300
    for b1,b2 in combinations(boxes, 2):
        # d = dist(b1, b2)
        # print(b1, b2, d)
        if (d := dist(b1, b2)) < min_dist:
            min_dist = d
            best_pair = b1, b2

    print(best_pair)

main()
