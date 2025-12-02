from sys import argv
import re

with open(argv[1]) as f:
    ranges = [[int(d) for d in p.split('-')] for p in [pair for pair in f.read().rstrip().split(',')]]

part1 = 0
part2 = 0
for r in ranges:
    for id in range(r[0], r[1]+1):
        id_str = str(id)
        if re.fullmatch(r'(\d+)\1', id_str):
            part1 += id

        if re.fullmatch(r'(\d+)\1+', id_str):
            part2 += id

print('Part 1:', part1)
print('Part 2:', part2)


    

    
