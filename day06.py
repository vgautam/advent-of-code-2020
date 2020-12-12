#!/usr/bin/env python3
from functools import reduce

groups = [[set(p) for p in g.split()] for g in open('2020day06input').read().strip().split('\n\n')]
print(f'part 1\n{sum([len(reduce(lambda a, b: a.union(b), group)) for group in groups])}')
print(f'part 2\n{sum([len(reduce(lambda a, b: a.intersection(b), group)) for group in groups])}')
