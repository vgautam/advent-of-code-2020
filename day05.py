#!/usr/bin/env python3
import re
regex1 = re.compile(r'[BR]')
regex0 = re.compile(r'[LF]')

seats = [int(regex0.sub('0', regex1.sub('1', line.strip())), 2) for line in open('2020day05input')]
print(f'part 1\n{max(seats)}')
print(f'part 2\n{set(range(min(seats), max(seats))).difference(set(seats))}')
