#!/usr/bin/env python3
import re
import regex

day=19 # update me
inp_f = f'2020day{day:02d}input'
lines = [l.strip() for l in open(inp_f + '.rules')] # every line

replace_dict = {}
for line in lines:
    l = ''.join(re.sub(r'(\d+)', r'_\1_', line).split())
    _spl = l.replace('"', '').split(':')
    replace_dict[_spl[0]] = _spl[1]

def generate_regex(replace_dict, start_at='_0_'):
    nonterm = start_at
    monster_regex = '^' + replace_dict[nonterm] + '$'
    while re.search('_\d+_', monster_regex):
        next_nonterm = re.search('(_\d+_)', monster_regex).group(1)
        replacement = replace_dict[next_nonterm]
        if '|' in replacement:
            replacement = '(' + replacement + ')'
        monster_regex = monster_regex.replace(next_nonterm, replacement)
    return monster_regex

print('part 1')
monster_regex = generate_regex(replace_dict)
compiled = re.compile(monster_regex)
print(sum([1 for line in open(inp_f) if compiled.match(line)]))

print('part 2')
replace_dict['_8_'] = '(_42_)+'
replace_dict['_11_'] = '(?P<recurs>_42_(?P>recurs)?_31_)' # lost SO MUCH TIME because I thought
                                                          # (?R)? would work on its own, but no.
                                                          # named capturing groups ftw
monster_regex = generate_regex(replace_dict)
compiled = regex.compile('(?V1)' + monster_regex)
print(sum([1 for line in open(inp_f) if compiled.match(line)]))
