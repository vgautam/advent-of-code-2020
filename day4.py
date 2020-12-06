#!/usr/bin/env python3
import re

passports = [{f.split(':')[0]: f.split(':')[1] for f in p.split()} for p in open('2020day4input').read().split('\n\n')]
valid_passports = [p for p in passports if {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}.issubset(p.keys())]
print(f'part 1\n{len(valid_passports)}')

def valid(passport):
    try:
        assert int(passport['byr']) in range(1920,2003)
        assert int(passport['iyr']) in range(2010,2021)
        assert int(passport['eyr']) in range(2020,2031)
        assert re.match('^(1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in)$', passport['hgt'])
        assert re.match('^#[0-9a-f]{6}$', passport['hcl'])
        assert re.match('^[0-9]{9}$', passport['pid'])
        assert passport['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
        return True
    except AssertionError:
        return False
print(f'part 2\n{len([p for p in valid_passports if valid(p)])}')
