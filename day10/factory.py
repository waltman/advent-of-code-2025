import sys
from itertools import combinations_with_replacement

bits = {x: 2**x for x in range(15)}

def parse_target(target):
    result = 0
    for i in range(len(target)):
        if target[i] == '#':
            result += bits[i]
    return result

def parse_button(button):
    return sum([bits[int(x)] for x in button.split(',')])

def xor(arr):
    result = 0
    for val in arr:
        result ^= val

    return result

def main():
    bits = {x: 2**x for x in range(15)}
    targets = []
    buttons = []
    joltages = []
    with open(sys.argv[1]) as f:
        for line in f:
            toks = line.rstrip().split()
            targets.append(parse_target(toks[0][1:-1]))
            buttons.append([parse_button(toks[i][1:-1]) for i in range(1, len(toks)-1)])
            joltages.append(toks[-1])

    print(targets)
    print(buttons)
    print(joltages)

    part1 = 0
    for i in range(len(targets)):
        target = targets[i]
        b = buttons[i]
        presses = 0
        done = False
        while not done:
            presses += 1
            for comb in combinations_with_replacement(b, presses):
                if xor(comb) == target:
                    print(f'{i=} {presses=} {comb=}')
                    part1 += presses
                    done = True
                    print()
                    break

    print('Part 1', part1)

main()
