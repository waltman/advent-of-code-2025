import sys

regions = []
presents = []
with open(sys.argv[1]) as f:
    for line in f:
        # ignore the presents for now
        if len(line) < 3 or line[2] != 'x':
            continue
        
        toks = line.rstrip().split(': ')
        regions.append([int(x) for x in toks[0].split('x')])
        presents.append([int(x) for x in toks[1].split(' ')])

# let's check if anything fits
total = 0
easy = 0
impossible = 0
unknown = 0
sizes = [7, 5, 7, 6, 7, 7]
for i in range(len(regions)):
    area = regions[i][0] * regions[i][1]
    full = sum([n * 9 for n in presents[i]])
    packed = 0
    for j in range(len(presents[i])):
        packed += presents[i][j] * sizes[j]
    total = 0
    if area >= full:
        easy += 1
    elif area < packed:
        impossible += 1
    else:
        print(f'unknown! {area=} {full=} {packed=}')
        unknown += 1

print(easy, impossible, unknown, total)
# it turns out they're all easy!
print('Part 1:', easy)
