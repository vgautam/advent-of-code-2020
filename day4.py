#!/usr/bin/env python3

import re
required_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
optional_keys = {'cid'}

print('part 1')
num_valid_passports = 0
with open('2020day4input', 'r', encoding='utf-8') as fo:
    for passport in fo.read().split('\n\n'):
        #print(passport)
        #print()
        present_keys = set()
        for entry in passport.split():
            k,v = entry.split(':')
            #print(k)
            present_keys.add(k)
        if present_keys.intersection(required_keys) == required_keys:
            num_valid_passports += 1
print(num_valid_passports)

print('part 2')
def is_valid(key, value):
    if key == 'byr':
        return int(value) >= 1920 and int(value) <= 2002
    elif key == 'iyr':
        return int(value) >= 2010 and int(value) <= 2020
    elif key == 'eyr':
        return int(value) >= 2020 and int(value) <= 2030
    elif key == 'hgt':
        match = re.match('^(\d+)(cm|in)$', value)
        if match:
            if match.group(2) == 'cm' and int(match.group(1)) >= 150 and int(match.group(1)) <= 193:
                return True
            elif match.group(2) == 'in' and int(match.group(1)) >= 59 and int(match.group(1)) <= 76:
                return True
        return False
    elif key == 'hcl':
        match = re.match('^#[0-9a-f]{6}$', value)
        if match:
            return True
        return False
    elif key == 'ecl':
        return value in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    elif key == 'pid':
        match = re.match('^[0-9]{9}$', value)
        if match:
            return True
        return False
    return True

num_valid_passports = 0
with open('2020day4input', 'r', encoding='utf-8') as fo:
    for passport in fo.read().split('\n\n'):
        passport_dict = {}
        for entry in passport.split():
            k,v = entry.split(':')
            passport_dict[k] = v
        present_keys = set(passport_dict.keys())
        if present_keys.intersection(required_keys) == required_keys:
            #print([(k, v, is_valid(k,v)) for k,v in passport_dict.items()])
            if all([is_valid(k,v) for k,v in passport_dict.items()]):
                num_valid_passports += 1
            #else:
                #print(passport_dict)
print(num_valid_passports)

assert(is_valid('pid', '000000001'))
assert(is_valid('ecl', 'brn'))
assert(is_valid('hcl', '#123abc'))
assert(is_valid('byr', '2002'))
assert(is_valid('hgt', '60in'))
assert(is_valid('hgt', '190cm'))

assert(not is_valid('pid', '0123456789'))
assert(not is_valid('ecl', 'wat'))
assert(not is_valid('hcl', '123abc'))
assert(not is_valid('hcl', '123abz'))
assert(not is_valid('hgt', '60cm'))
assert(not is_valid('hgt', '190in'))
assert(not is_valid('byr', '2003'))
