from sys import argv
from itertools import combinations

with open(argv[1]) as f:
    banks = [[int(c) for c in line.rstrip()] for line in f]

part1 = sum([max([n1*10 + n2 for n1,n2 in combinations(bank, 2)]) for bank in banks])
print('Part 1:', part1)

part2 = 0
for bank in banks:
    bank2 = ''.join([str(n) for n in bank])
    print(bank2)
    best = 0
    for comb in combinations(bank2, 12):
        best = max(best, int(''.join(comb)))
    part2 += best
    
print('Part 2:', part2)
