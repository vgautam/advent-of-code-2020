#!/usr/bin/env python3

day=23 # update me
inp_f = f'2020day{day:02d}input'

lines = [int(c) for c in open(inp_f).read().strip()]
lines = [int(c) for c in '389125467']

_min = min(lines)
l = len(lines)

print('part 1')
def crab_game(lines, num_moves):
    i = 0
    for iteration in range(num_moves):
        cup = lines[i]
        should_be_next = lines[(i+4)%l]
        displaced_cups = []
        for _ in range(3):
            d_c = lines.pop((lines.index(cup)+1)%len(lines))
            displaced_cups.append(d_c)
        _sorted = sorted(lines)
        destination = _sorted[_sorted.index(cup)-1]
        replace_after = lines.index(destination)
        displaced_cups.reverse()
        for d_c in displaced_cups:
            lines.insert((replace_after+1)%l, d_c)
        i = (i+1)%l
        while not lines[i] == should_be_next:
            lines = lines[1:] + [lines[0]]
        assert lines[i] == should_be_next
    return lines

lines = crab_game(lines, 100)
while not lines[0] == 1:
    lines = lines[1:] + [lines[0]]
print(''.join([str(c) for c in lines[1:]]))

print('part 2')
# it's pretty clear this isn't going to work
# the q is: do i now implement my own linked list from scratch or do i use a python builtin?
# (also does one exist)
_max = max(lines)
for i in range(_max+1,1000001):
    lines.append(i)
lines = crab_game(lines, 10000000)
i = lines.index(1)
print(lines[(i+1) % len(lines)])
print(lines[(i+1) % len(lines)])
