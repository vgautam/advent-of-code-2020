#!/usr/bin/env python3
from functools import reduce

print('part 1')
num_yeses = []
with open('2020day6input', 'r', encoding='utf-8') as fo:
    lines = fo.read().strip().split('\n\n')
    for line in lines:
        num_yeses.append(len(set(''.join(line.split()))))
print(sum(num_yeses))

print('part 2')
num_yeses = []
with open('2020day6input', 'r', encoding='utf-8') as fo:
    lines = fo.read().strip().split('\n\n')
    for line in lines:
        yeses = []
        for person in line.split():
            yeses.append(set(person))
            #print(yeses)
        num_yeses.append(len(reduce(lambda a, b: a.intersection(b), yeses)))
print(sum(num_yeses))
