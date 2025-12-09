import sys
from itertools import combinations

def area(t1, t2):
    return abs(t1[0]-t2[0]+1) * abs(t1[1]-t2[1]+1)

def main():
    with open(sys.argv[1]) as f:
        tiles = [[int(d) for d in line.rstrip().split(',')] for line in f]

    print('Part 1:', max([area(t1, t2) for t1, t2 in combinations(tiles, 2)]))

main()
