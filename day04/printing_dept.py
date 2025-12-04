import sys
import numpy as np
from itertools import product

def neighbors(grid, row, col):
    deltas = [
        [-1,-1],
        [-1, 0],
        [-1, 1],
        [ 0,-1],
        [ 0, 1],
        [ 1,-1],
        [ 1, 0],
        [ 1, 1],
    ]
    nrows, ncols = grid.shape
    for delta in deltas:
        r = row + delta[0]
        c = col + delta[1]
        if r >= 0 and r < nrows and c >= 0 and c < ncols:
            yield(r, c)

def num_adjacent(grid, row, col):
    cnt = 0
    for r,c in neighbors(grid, row, col):
        if grid[r,c] == '@':
            cnt += 1
    return cnt

def main():
    with open(sys.argv[1]) as f:
        grid = np.array([[c for c in line.rstrip()] for line in f])
    nrows, ncols = grid.shape

    part1 = 0
    for r,c in product(range(nrows), range(ncols)):
        if grid[r,c] == '@' and num_adjacent(grid, r, c) < 4:
            part1 += 1

    print('Part 1:', part1)

    part2 = 0
    done = False
    while not done:
        rows = []
        cols = []
        for r,c in product(range(nrows), range(ncols)):
            if grid[r,c] == '@' and num_adjacent(grid, r, c) < 4:
                part2 += 1
                rows.append(r)
                cols.append(c)

        if rows:
            grid[rows,cols] = '.'
        else:
            done = True

    print('Part 2:', part2)

main()
