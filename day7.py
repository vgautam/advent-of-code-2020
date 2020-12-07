#!/usr/bin/env python3

import re

rules = {}
with open('2020day7input', 'r', encoding='utf-8') as fo:
    for line in fo:
        _spl = line.split(' contain ')
        rules[_spl[0].split(' bags')[0]] = _spl[1].strip()

def get_bags_holding(bag):
    bags = set()
    for k,v in rules.items():
        if bag in v:
            bags.add(k)
    return bags

def recurse(bag):
    holding_bags = set()
    holding = get_bags_holding(bag)
    print(bag, ': ', holding)
    holding_bags.update(holding)
    print(holding_bags)
    if len(holding) > 0:
        for bag in holding:
            holding_bags.update(recurse(bag))
    return holding_bags

print(get_bags_holding('shiny gold'))
print(recurse('shiny gold'))
print(len(recurse('shiny gold')))
print('part 1')


def get_bags_holding(bag):
    bags = []
    for raw in rules[bag].split(','):
        for b in re.finditer('(\d+) (\w+ \w+)', raw):
            bags += [b.group(2)]*int(b.group(1))
    return bags

def recurse(bag):
    holding_bags = []
    holding = get_bags_holding(bag)
    print(bag, ': ', holding)
    holding_bags += holding
    print(holding_bags)
    if len(holding) > 0:
        for bag in holding:
            holding_bags += recurse(bag)
    return holding_bags

print(get_bags_holding('shiny gold'))
print(recurse('shiny gold'))
print(len(recurse('shiny gold')))
print('part 2')
