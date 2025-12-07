import sys
import numpy as np

def main():
    with open(sys.argv[1]) as f:
        grid = np.array([[c for c in line.rstrip()] for line in f])
    nrows, ncols = grid.shape

    # find the initial column of the beam
    for col in range(ncols):
        if grid[0,col] == 'S':
            beams = {col}
            break
    
    # now track the beam as it goes down
    part1 = 0
    for row in range(1, nrows):
        new_beams = set()
        for col in range(ncols):
            if col in beams:
                if grid[row,col] == '^':
                    new_beams.add(col-1)
                    new_beams.add(col+1)
                    part1 += 1
                else:
                    new_beams.add(col)
        beams = new_beams.copy()

    print('Part 1:', part1)

main()
