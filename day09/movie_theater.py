import sys
from itertools import combinations
import shapely

def area(t1, t2):
    return (abs(t1[0]-t2[0])+1) * (abs(t1[1]-t2[1])+1)

def box(t1, t2):
    xmin = min(t1[0], t2[0])
    xmax = max(t1[0], t2[0])
    ymin = min(t1[1], t2[1])
    ymax = max(t1[1], t2[1])

    return shapely.box(xmin, ymin, xmax, ymax)

def main():
    with open(sys.argv[1]) as f:
        tiles = [[int(d) for d in line.rstrip().split(',')] for line in f]

    print('Part 1:', max([area(t1, t2) for t1, t2 in combinations(tiles, 2)]))

    border = shapely.Polygon(tiles)

    part2 = 0
    for t1, t2 in combinations(tiles, 2):
        this_area = area(t1, t2)
        b1 = box(t1, t2)
        if this_area > part2 and not shapely.overlaps(border, b1):
            print('new best', this_area)
            part2 = this_area
    print('Part 2:', part2)

main()
