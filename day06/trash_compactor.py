import sys
import numpy as np
from math import prod

def main():
    rows = []
    raw = []
    with open(sys.argv[1]) as f:
        for line in f:
            toks = line.split()
            if toks[0].isnumeric():
                rows.append([int(tok) for tok in toks])
                raw.append(line)
            else:
                ops = toks

    grid = np.array(rows)
    ncols = grid.shape[1]
    part1 = 0
    for col in range(ncols):
        if ops[col] == '+':
            part1 += np.sum(grid[:,col])
        else:
            part1 += np.prod(grid[:,col])

    print('Part 1:', part1)

    # turn the raw grid into the values for part 2
    ncols = len(raw[0]) - 1
    vals = []
    cols = []
    for col in range(ncols):
        val_str = ''
        for row in range(len(raw)):
            val_str += raw[row][col]
        val_str = val_str.strip()
        if val_str == '':
            cols.append(vals.copy())
            vals.clear()
        else:
            vals.append(int(val_str))
    cols.append(vals.copy())

    part2 = 0
    for col in range(len(cols)):
        if ops[col] == '+':
            part2 += sum(cols[col])
        else:
            part2 += prod(cols[col])

    print('Part 2:', part2)
    
main()
