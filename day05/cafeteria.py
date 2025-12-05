import sys

def merge_ranges(ranges):
    ranges.sort()
    result = [ranges[0]]
    for curr in ranges[1:]:
        last = result[-1]
 
        if curr[0] <= last[1]:
            # curr overlaps last, so (possibly) extend last
            last[1] = max(last[1], curr[1])
        else:
            # no overlap, so add curr as the last range
            result.append(curr)

    return result

def main():
    ranges = []
    ids = []
    state = 1

    with open(sys.argv[1]) as f:
        for line in f:
            line = line.rstrip()
            if line == '':
                state = 2
            elif state == 1:
                ranges.append([int(n) for n in line.split('-')])
            else:
                ids.append(int(line))

    part1 = 0
    for val in ids:
        for n1, n2 in ranges:
            if n1 <= val <= n2:
                part1 += 1
                break

    print('Part 1:', part1)

    merged = merge_ranges(ranges)
    part2 = sum([r[1]-r[0]+1 for r in merged])
    print('Part 2:', part2)

main()
