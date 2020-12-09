#!/usr/bin/env python3

lines = [int(l) for l in open('2020day9input').read().split()]

def is_sum_possible(options, _sum):
    for i in options:
        if _sum - i in options and _sum - i != i:
            return True
    return False

stepsize = 25
for i in range(stepsize, len(lines)):
    if not is_sum_possible(lines[i-stepsize:i], lines[i]):
        imposs_idx = i
        imposs_num = lines[imposs_idx]
        break
print(f'part 1: {imposs_num}')

def get_continuous_sublist(numbers, target_sum):
    length = len(numbers)
    for i in range(length):
        for j in range(i+1, length):
            options = numbers[i:j+1]
            _sum = sum(options)
            if _sum == target_sum:
                return options
            if _sum > target_sum:
                break

sublist = get_continuous_sublist(lines[:imposs_idx], imposs_num)
print(f'part 2: {min(sublist) + max(sublist)}')
