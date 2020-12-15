#!/usr/bin/env python3
from collections import defaultdict

day=15 # update me
lines = [0,5,4,1,10,14,7]
#lines = [0,3,6]

last_seen = defaultdict(lambda:-1)
print(lines)

print('part 1')
for i,spoken in enumerate(lines[:-1]):
    print(spoken)
    last_seen[spoken] = i

last_num = lines[-1]
print(last_num)
for i in range(len(last_seen),30000000-1):
    last_num_last_seen = last_seen[last_num]
    if last_num_last_seen == -1:
        spoken = 0
    else:
        spoken = i - last_num_last_seen
    print(i, spoken)
    last_seen[last_num] = i
    last_num = spoken

print('final', spoken)

print('part 2')
