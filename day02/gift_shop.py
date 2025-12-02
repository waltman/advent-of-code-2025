from sys import argv

def is_invalid(id):
    size = len(id) // 2
    return id[:size] == id[size:]

with open(argv[1]) as f:
    ranges = [[int(d) for d in p.split('-')] for p in [pair for pair in f.read().rstrip().split(',')]]

part1 = 0
for r in ranges:
    for id in range(r[0], r[1]+1):
        id_str = str(id)
        if len(id_str) % 2 == 0 and is_invalid(id_str):
            part1 += id

print('Part 1:', part1)


    

    
