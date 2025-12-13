import sys
from itertools import combinations

def area(t1, t2):
    return (abs(t1[0]-t2[0])+1) * (abs(t1[1]-t2[1])+1)

def line_points(t1, t2):
    if t1[0] == t2[0]: # horizontal
        start = min(t1[1], t2[1])
        end = max(t1[1], t2[1])
        for col in range(start, end):
            yield((t1[0], col))
    else: # vertical
        start = min(t1[0], t2[0])
        end = max(t1[0], t2[0])
        for row in range(start, end):
            yield((row, t1[1]))

def main():
    with open(sys.argv[1]) as f:
        tiles = [[int(d) for d in line.rstrip().split(',')] for line in f]

    print('Part 1:', max([area(t1, t2) for t1, t2 in combinations(tiles, 2)]))

    # make a set with all the points along the edges
    edges = set()
    for t in tiles:
        edges.add(tuple(t))
        
    for i in range(len(tiles)):
        x = i
        y = (i+1) % len(tiles)
        for p in line_points(tiles[x], tiles[y]):
            edges.add(p)

    # find the extend of the tiles
    min_row, min_col = 1e300, 1e300
    max_row, max_col = -1, -1

    for tile in tiles:
        min_row = min(min_row, tile[0])
        max_row = max(max_row, tile[0])
        min_col = min(min_col, tile[1])
        max_col = max(max_col, tile[1])

    min_row -= 1
    min_col -=1
    max_row += 1
    max_col += 1

    # now let's try to solve it!
    best = 0
    for t1, t2 in combinations(tiles, 2):
        this_area = area(t1, t2)
        print('testing', t1, t2, this_area)
        if this_area < best:
            print('too small')
            continue

        min_r = min(t1[0], t2[0])
        min_c = min(t1[1], t2[1])
        max_r = max(t1[0], t2[0])
        max_c = max(t1[1], t2[1])
        good = True
        
        for r in range(min_r, max_r+1):
            hit_border = False
            for c in range(min_c, max_c+1):
                if (r,c) in edges:
                    continue
                # left
                for c1 in range(c-1, min_col-1, -1):
                    if (r, c1) in edges:
                        break
                    elif c1 == min_col:
#                        print('failed left', r, c)
                        hit_border = True
                if hit_border:
                    break
                
                # right
                for c1 in range(c+1, max_col+1):
                    if (r, c1) in edges:
                        break
                    elif c1 == max_col:
#                        print('failed right', r, c)
                        hit_border = True
                if hit_border:
                    break
                
                # up
                for r1 in range(r-1, min_row-1, -1):
                    if (r1, c) in edges:
                        break
                    elif r1 == min_row:
#                        print('failed up', r, c)
                        hit_border = True
                if hit_border:
                    break
                
                # down
                for r1 in range(r+1, max_row-1, -1):
                    if (r1, c) in edges:
                        break
                    elif r1 == max_row:
#                        print('failed down', r, c)
                        hit_border = True
                if hit_border:
                    break
            if hit_border:
                good = False
                break
        if good:
            print('new best', this_area, t1, t2)
            best = this_area

    print('Part 2:', best)
#    print((2,4) in edges)
#    print(edges)
#    print(min_c)

main()
