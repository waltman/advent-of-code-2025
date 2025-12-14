import sys
import networkx as nx
from math import prod
from functools import cache

def paths_between(from_set, to_set, too_far, DG):
    stack = [f for f in from_set]
    cnt = 0
    while stack:
        node = stack.pop()
        if node in to_set:
            cnt += 1
        elif node not in too_far:
            stack += DG.neighbors(node)

    return cnt

# This is an elegant solution I found on reddit which works whem my code wasn't.
# Full code at https://github.com/mnvr/aoc-25/blob/main/11.py
@cache
def path_count(node, dest, DG):
    if node == dest:
        return 1
    else:
        return sum(path_count(v, dest, DG) for v in DG.neighbors(node))

def main():
    outputs = dict()
    with open(sys.argv[1]) as f:
        for line in f:
            device = line[0:3]
            outs = [tok for tok in line[5:].rstrip().split(' ')]
            outputs[device] = outs

    DG = nx.DiGraph()
    for k,v in outputs.items():
        for node in v:
            DG.add_edge(k, node)

    part2 = []
#    stack = [('svr', False, False)]
    stack = [('fft', False, False)]
    fft_set = {'hju', 'tvs', 'kow', 'une'}
    dac_set = {'you', 'bbg', 'fwk', 'gia', 'zvu'}
    part2.append(paths_between({'svr'}, {'fft'}, fft_set, DG))
    part2.append(paths_between({'fft'}, fft_set, {}, DG))
    part2.append(paths_between(fft_set, {'zkr', 'lka', 'tth', 'hlr', 'aps'}, {}, DG))
    part2.append(paths_between({'zkr', 'lka', 'tth', 'hlr', 'aps'}, {'nfe', 'mzm', 'hlc'}, {}, DG))
    part2.append(paths_between({'nfe', 'mzm', 'hlc'}, {'dac'}, dac_set, DG))
    part2.append(paths_between({'dac'}, dac_set, {}, DG))
    part2.append(paths_between(dac_set, {'out'}, {}, DG))

    print('Part 2:', part2, prod(part2))

    stack = [('svr', False)]
    cnt = 0
    hit = set()
    while stack:
        node, seen_fft = stack.pop()
        if node == 'fft':
            seen_fft = True
        if node in fft_set:
            if seen_fft:
                cnt += 1
                hit.add(node)
        else:
            for n in DG.neighbors(node):
                stack.append((n, seen_fft))

    print(cnt, hit)

    stack = [(node, False) for node in ['nfe', 'mzm', 'hlc']]
    cnt = 0
    hit = set()
    while stack:
        node, seen_dac = stack.pop()
        if node == 'dac':
            seen_dac = True
        if node == 'out':
            if seen_dac:
                cnt += 1
                hit.add(node)
        else:
            for n in DG.neighbors(node):
                stack.append((n, seen_dac))

    print(cnt, hit)

    from_set = {'hju', 'tvs', 'kow', 'une'}
    to_set = {'nfe', 'mzm', 'hlc'}
    stack = [(node, False) for node in from_set]
    cnt = 0
    hit = set()
    while stack:
        node, seen_dac = stack.pop()
        if node in to_set:
            cnt += 1
            hit.add(node)
        else:
            for n in DG.neighbors(node):
                stack.append((n, seen_dac))

    print(cnt, hit)

    # This is the part that finally worked!
    print('Part 2:', path_count('svr', 'fft', DG) * path_count('fft', 'dac', DG) * path_count('dac', 'out', DG))
          
main()
