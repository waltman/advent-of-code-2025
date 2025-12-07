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
            stack = [(0, col,[(0,col)])]
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

    part2 = 0
    timelines = set()
    while stack:
        row, col, path = stack.pop()
        new_path = path + [(row, col)]
#        print(f'checking {row} {col} {new_path}')
        if tuple(new_path) not in timelines:
#            print('adding')
            timelines.add(tuple(path))
            if row == nrows-1:
                part2 += 1
            elif grid[row,col] == '^':
                stack.append((row, col-1, path + [(row+1, col-1)]))
                stack.append((row, col+1, path + [(row+1, col+1)]))
            else:
                # keep going until we hit a splitter or the bottom
                done = True
                for r in range(row+1, nrows):
                    if grid[r,col] == '^':
                        stack.append((r, col-1, path + [(r+1, col-1)]))
                        stack.append((r, col+1, path + [(r+1, col-1)]))
                        done = False
                        break
                if done:
                    part2 += 1
                    print(part2, len(stack), len(timelines))
        else:
            print('skipping')

    print('Part 2:', part2)

main()
