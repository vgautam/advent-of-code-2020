#!/usr/bin/env python3

lines = open('2020day12input').read().split() # every word

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

def turn(coords, direction, magnitude):
    assert magnitude in [90, 180, 270], magnitude
    if magnitude == 180:
        return (-coords[0], -coords[1])
    elif magnitude == 90:
        if direction == 'R':
            return (-coords[1], coords[0])
        return (coords[1], -coords[0])
    return turn(turn(coords, direction, 180), direction, 90)

# print(turn((10,5), 'L', 180))
# print(turn((10,5), 'R', 180))
# print(turn((10,5), 'L', 90))
# print(turn((10,5), 'R', 90))
# print(turn((10,5), 'L', 270))
# print(turn((10,5), 'R', 270))

def move(coords, direction, magnitude):
    mapping = {'E': (coords[0], coords[1]+magnitude),
               'W': (coords[0], coords[1]-magnitude),
               'N': (coords[0]+magnitude, coords[1]),
               'S': (coords[0]-magnitude, coords[1])}
    if direction in ['L', 'R']:
        return turn(coords, direction, magnitude)
    return mapping[direction]

coords = (0,0)
wp_coords = (1,10)
for l in lines:
    #print(coords, wp_coords, l)
    direction = l[0]
    magnitude = int(l[1:])
    if direction != 'F':
        wp_coords = move(wp_coords, direction, magnitude)
    else:
        coords = (coords[0] + magnitude*wp_coords[0], coords[1] + magnitude*wp_coords[1])

print(abs(coords[0])+abs(coords[1]))
