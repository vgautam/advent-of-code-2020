#!/usr/bin/env python3

lines = open('2020day12input').read().split() # every word
#lines = open('test').read().split() # every word
#lines = open('2020day7input').readlines() # every line + \n
#lines = [l.strip() for l in open('2020day7input')] # every line
#lines = [l.strip() for l in open('2020day7input').read().split('\n\n')] # every block separated by 2 newlines
#lines = [l.split() for l in open('2020day7input').read().split('\n\n')] # every block separated by 2 newlines, split into words

#print(lines)
print('part 1')

def turn(facing, direction, magnitude):
    assert magnitude in [90, 180, 270], magnitude
    l_mapping = {'E': 'N', 'S': 'E', 'N': 'W', 'W': 'S'}
    r_mapping = {'E': 'S', 'S': 'W', 'N': 'E', 'W': 'N'}
    _180_mapping = {'E': 'W', 'N': 'S', 'W': 'E', 'S': 'N'}
    if direction == 'L' and magnitude == 90:
        return l_mapping[facing]
    if direction == 'R' and magnitude == 90:
        return r_mapping[facing]
    if magnitude == 270:
        return turn(_180_mapping[facing], direction, magnitude-180)
    return _180_mapping[facing]

def move(coords, direction, facing, magnitude):
    mapping = {'E': (coords[0], coords[1]+magnitude),
               'W': (coords[0], coords[1]-magnitude),
               'N': (coords[0]+magnitude, coords[1]),
               'S': (coords[0]-magnitude, coords[1])}
    if direction == 'F':
        coords = mapping[facing]
    elif direction in ['L', 'R']:
        facing = turn(facing, direction, magnitude)
    else:
        coords = mapping[direction]
    return coords, facing

facing = 'E'
coords = (0,0)
for l in lines:
    direction = l[0]
    magnitude = int(l[1:])
    coords, facing = move(coords, direction, facing, magnitude)

print(abs(coords[0])+abs(coords[1]))

print('part 2')
