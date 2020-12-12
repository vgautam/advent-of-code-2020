#!/usr/bin/env python3

import re

rules = {}
for line in open('2020day07input'):
    v = [m.group(2) for m in re.finditer('(\d+) (\w+ \w+)', line) for n in range(int(m.group(1)))]
    rules[re.match('^\w+ \w+', line).group()] = v

def get_bags_containing(bag):
    return {k for k in rules if bag in rules[k]}

def recurse(bag, func):
    bags = []
    current_bags = list(func(bag))
    bags += current_bags
    if len(current_bags) > 0:
        for b in current_bags:
            bags += recurse(b, func)
    return bags

print(f"part 1: {len(set(recurse('shiny gold', get_bags_containing)))}")
print(f"part 2: {len(recurse('shiny gold', rules.get))}")
