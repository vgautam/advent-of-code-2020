#!/usr/bin/env python3

numbers = [int(l.strip()) for l in open('2020day01input')]

def part1(numbers, target_sum):
    for n in numbers:
        if target_sum - n in numbers:
            return n * (target_sum - n)

print('part1:', part1(numbers, 2020))

def part2(numbers, target_sum):
    for n in numbers:
        res = part1(numbers, target_sum - n)
        if res:
            return n * res

print('part2:', part2(numbers, 2020))
