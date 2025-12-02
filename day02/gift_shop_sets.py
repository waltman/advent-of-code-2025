from sys import argv
from itertools import product

with open(argv[1]) as f:
    ranges = [[int(d) for d in p.split('-')] for p in [pair for pair in f.read().rstrip().split(',')]]

pairs = {int(str(x) * 2) for x in range(1, 100_000)}

dups = pairs.copy()
# 3 copies
dups |= {int(str(i) * 3) for i in range(1,1000)}

# 4-5 copies
dups |= {int(str(i) * copies) for i,copies in product(range(1,100), range(4,6))}

# 6-10 copies
dups |= {int(str(i) * copies) for i,copies in product(range(1,10), range(6,11))}

part1 = 0
part2 = 0
for r in ranges:
    part1 += sum(set(range(r[0], r[1]+1)) & pairs)
    part2 += sum(set(range(r[0], r[1]+1)) & dups)

print('Part 1:', part1)
print('Part 2:', part2)
