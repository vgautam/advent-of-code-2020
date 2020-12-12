#!/usr/bin/env python3
import re

lines = [re.sub('[:-]', ' ', line).split() for line in open('2020day2input')]
print(f'part 1: {len([l for l in lines if l[3].count(l[2]) in range(int(l[0]) , int(l[1])+1)])}')
print(f'part 2: {len([l for l in lines if (l[3][int(l[0])-1] == l[2]) != (l[3][int(l[1])-1] == l[2])])}')
