#!/usr/bin/env python3

lines = [int(l) for l in open('2020day9input').read().split()]

def is_sum_possible(options, _sum):
    for i in options:
        if _sum - i in set(options) and _sum - i != i:
            return True
    return False

stepsize = 25
for i in range(stepsize, len(lines)):
    if not is_sum_possible(lines[i-stepsize:i], lines[i]):
        imposs_idx = i
        imposs_num = lines[imposs_idx]
        break
print(f'part 1: {imposs_num}')

def get_contiguous_sublists(numbers):
    length = len(numbers)
    for i in range(length):
        for j in range(i+1, length):
            yield numbers[i:j+1]

for options in get_contiguous_sublists(lines[:imposs_idx]):
    if sum(options) == imposs_num:
        print(f'part 2: {min(options) + max(options)}')
        break
