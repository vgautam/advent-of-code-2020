#!/usr/bin/env python3

lines = [int(l) for l in open('2020day10input').read().split()] # every word

def lowest_acceptable_adapter(adapters, voltage):
    if (voltage+1) in adapters:
        return voltage+1
    if voltage+2 in adapters:
        return voltage+2
    if voltage+3 in adapters:
        return voltage+3
    raise ValueError

print('part 1')
def part1(lines):
    start = 0
    i = start
    adapters = lines
    differences = []
    order = [start]
    while True:
        _next = lowest_acceptable_adapter(adapters, i)
        differences.append(_next-i)
        order.append(_next)
        i = _next
        adapters.remove(_next)
        #print(adapters)
        if not adapters:
            break
    differences.append(3)
    order.append(165)
    return differences, order

differences, _ = part1([i for i in lines])
print(differences.count(1)*differences.count(3))

print('part 2')

sl = sorted(lines)

def get_list_with_next_item(fixed, adapters):
    opts = []
    if fixed[-1] + 1 in adapters:
        opts.append(fixed + [fixed[-1]+1])
    if fixed[-1] + 2 in adapters:
        opts.append(fixed + [fixed[-1]+2])
    if fixed[-1] + 3 in adapters:
        opts.append(fixed + [fixed[-1]+3])
    return opts

def recurse(fixed, adapters):
#    print(fixed)
    _max = max(adapters)
    acc = 0
    next_lists = get_list_with_next_item(fixed, adapters)
    if next_lists:
        for next_list in next_lists:
            latest_num = next_list[-1]
#            print(next_list, acc)
            if _max in next_list:
                acc += 1
            else:
                if cache[latest_num] == -1:
                    paths_from_latest_num = recurse(next_list, adapters)
                    cache[latest_num] = paths_from_latest_num
                acc += cache[latest_num]
    return acc

from collections import defaultdict
#sl = [16,10,15,5,1,11,7,19,6,12,4]
def default(): return -1
cache = defaultdict(default)
print(recurse([0], [0] + sl))
