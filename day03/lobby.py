from sys import argv
from itertools import combinations

def best_joltage(bank):
    joltage = 0
    pos = 0
    for i in range(12):
        remaining = 12-i
        last_n = len(bank) - remaining + 1
        best_val = 0
        for n in range(pos, last_n):
            if bank[n] > best_val:
                best_val = bank[n]
                best_pos = n
            if best_val == 9:
                break
        joltage = joltage * 10 + best_val
        pos = best_pos + 1

    return joltage

with open(argv[1]) as f:
    banks = [[int(c) for c in line.rstrip()] for line in f]

part1 = sum([max([n1*10 + n2 for n1,n2 in combinations(bank, 2)]) for bank in banks])
print('Part 1:', part1)

part2 = sum([best_joltage(bank) for bank in banks])
print('Part 2:', part2)
