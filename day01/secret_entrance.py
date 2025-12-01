from sys import argv

part1 = 0
part2 = 0
pos = 50
pos2 = 50
with open(argv[1]) as f:
    for line in f:
        direction = 1 if line[0] == 'R' else -1
        cnt = int(line[1:])
        pos = (pos + (cnt * direction)) % 100
        if pos == 0:
            part1 += 1

        for _ in range(cnt):
            pos2 = (pos2 + direction) % 100
            if pos2 == 0:
                part2 += 1

print('Part 1:', part1)
print('Part 2:', part2)
