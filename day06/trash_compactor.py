import sys
import numpy as np

def main():
    rows = []
    with open(sys.argv[1]) as f:
        for line in f:
            toks = line.split()
            if toks[0].isnumeric():
                rows.append([int(tok) for tok in toks])
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
    
main()
