#!/usr/bin/env python3
import re

day=19 # update me
inp_f = f'2020day{day:02d}input'
#inp_f = 'test'

#lines = open(inp_f).read().split() # every word
#lines = open(inp_f).readlines() # every line + \n
lines = [l.strip() for l in open(inp_f + '.rules')] # every line
#lines = [l.strip() for l in open(inp_f).read().split('\n\n')] # every block separated by 2 newlines
#lines = [l.split() for l in open(inp_f).read().split('\n\n')] # every block separated by 2 newlines, split into words

#print(lines)

print('part 1')
replace_dict = {}
for line in lines:
    l = ''.join(re.sub(r'(\d+)', r'_\1_', line).split())
    l = l.replace('"', '')
    _spl = l.split(':')
    replace_dict[_spl[0]] = _spl[1]

#print(replace_dict)
nonterm = '_0_'
monster_regex = '^' + replace_dict.pop(nonterm) + '$'
while not re.match('^\^[ab\(\)|]+\$$', monster_regex):
    next_nonterm = re.search('(_\d+_)', monster_regex).group(1)
    replacement = replace_dict[next_nonterm]
    if '|' in replacement:
        replacement = '(' + replacement + ')'
    monster_regex = monster_regex.replace(next_nonterm, replacement)

compiled = re.compile(monster_regex)
print(compiled)
print(sum([1 for line in open(inp_f) if compiled.match(line)]))

print('part 2')
