#!/usr/bin/env python3
import re
from functools import reduce

day=16 # update me
inp_f = f'2020day{day:02d}input'
#inp_f = 'test'

error_rate = 0

valid_ranges = {}
tickets = []
with open(inp_f) as fo:
    while True:
        line = fo.readline().strip()
        m = re.match('^(.*): (\d+)-(\d+) or (\d+)-(\d+)$', line)
        if not m:
            break
        valid_ranges[m.group(1)] = [range(int(m.group(2)), int(m.group(3))+1), range(int(m.group(4)), int(m.group(5))+1)]
    tickets = [l.strip().split(',') for l in fo.readlines()if ',' in l]

my_ticket = tickets[0]
other_tickets = tickets[1:]

print('part 1')
def valid_number(num):
    valid = False
    for k in valid_ranges:
        ranges = valid_ranges[k]
        if num in ranges[0] or num in ranges[1]:
            valid = True
            break
    return valid

#print(valid_number(1))
#print(valid_number(33))

valid_tickets = []
for ticket in other_tickets:
    valid = True
    for entry in ticket:
        if not valid_number(int(entry)):
            valid = False
            error_rate += int(entry)
    if valid:
        valid_tickets.append(ticket)
print(error_rate)

print('part 2')
def try_col(key, values):
    ranges = valid_ranges[key]
    for val in values:
        if not (int(val) in ranges[0] or int(val) in ranges[1]):
            return False
    return True

tickets = valid_tickets
col_mapping = {}
while len(col_mapping) < len(tickets[0]):
    for i in range(len(tickets[0])):
        values = [ticket[i] for ticket in tickets]
        candidate_cols = []
        for key in valid_ranges:
            if key not in col_mapping and try_col(key, values):
                candidate_cols.append(key)
        if len(candidate_cols) == 1:
            col_mapping[candidate_cols[0]] = i

indices = [col_mapping[key] for key in col_mapping if 'departure' in key]
print(reduce(lambda a,b: a*b, [int(my_ticket[index]) for index in indices]))
