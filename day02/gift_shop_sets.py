from sys import argv
import re

with open(argv[1]) as f:
    ranges = [[int(d) for d in p.split('-')] for p in [pair for pair in f.read().rstrip().split(',')]]

pairs = {int(str(x) * 2) for x in range(1, 100_000)}

dups = pairs.copy()
# 3 copies
for i in range(1, 1000):
    dups.add(int(str(i) * 3))

# 4-5 copies
for i in range(1, 100):
    for copies in range(4, 6):
        dups.add(int(str(i) * copies))

# 6-10 copies
for i in range(1, 10):
    for copies in range(6, 11):
        dups.add(int(str(i) * copies))

part1 = 0
part2 = 0
for r in ranges:
    part1 += sum(list(set(range(r[0], r[1]+1)) & pairs))
    part2 += sum(list(set(range(r[0], r[1]+1)) & dups))

print('Part 1:', part1)
print('Part 2:', part2)
