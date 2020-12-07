#!/usr/bin/env python3
import re
from collections import defaultdict

rules = {}
contained_by_rules = defaultdict(set)
contains_rules = {}
for line in open('2020day7input'):
    bag = re.match('^\w+ \w+', line).group()
    items = [m.group(2) for m in re.finditer('(\d+) (\w+ \w+)', line) for n in range(int(m.group(1)))]
    rules[bag] = items
    items = {m.group(2): int(m.group(1)) for m in re.finditer('(\d+) (\w+ \w+)', line)}
    #print(items)
    contains_rules[bag] = items
    for item in items:
        contained_by_rules[item].add(bag)

#print(contained_by_rules)
#print(contains_rules)

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
