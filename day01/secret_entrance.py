from sys import argv

part1 = 0
part2 = 0
pos = 50
pos2 = 50
with open(argv[1]) as f:
    for line in f:
        sign = 1 if line[0] == 'R' else -1
        cnt = int(line[1:]) * sign
        pos = (pos + cnt) % 100
        if pos == 0:
            part1 += 1

        on_zero = pos2 == 0
        pos2 += cnt
        
        # did we cross 0 going backwards?
        if not on_zero and pos2 <= 0:
            part2 += 1

        # how many more times did we spin past 0?
        part2 += abs(pos2) // 100
        
        pos2 %= 100

print('Part 1:', part1)
print('Part 2:', part2)
