from sys import argv

def is_invalid(id, groups):
    size = len(id) // groups
    target = id[:size]
    for i in range(size, len(id), size):
        if id[i:i+size] != target:
            return False
    return True

with open(argv[1]) as f:
    ranges = [[int(d) for d in p.split('-')] for p in [pair for pair in f.read().rstrip().split(',')]]

part1 = 0
part2 = 0
for r in ranges:
    for id in range(r[0], r[1]+1):
        id_str = str(id)
        if len(id_str) % 2 == 0 and is_invalid(id_str, 2):
            part1 += id

        for i in range(2, len(id_str) + 1):
            if len(id_str) % i == 0 and is_invalid(id_str, i):
                part2 += id
                break

print('Part 1:', part1)
print('Part 2:', part2)


    

    
