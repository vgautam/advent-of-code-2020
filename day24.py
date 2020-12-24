#!/usr/bin/env python3
import re
from collections import defaultdict

day=24 # update me
inp_f = f'2020day{day:02d}input'
#inp_f = 'test24'

lines = [[d for d in re.split(r'(s[we]|n[we]|e|w)', l.strip()) if d] for l in open(inp_f)] # eh, it works

mappings = {'se': (-0.5,+0.5),
            'nw': (+0.5,-0.5),
            'ne': (+0.5,+0.5),
            'sw': (-0.5,-0.5),
            'e': (0,+1),
            'w': (0,-1)}

def apply(coords, shift):
    return (coords[0]+shift[0], coords[1]+shift[1])

tile_colours = defaultdict(lambda: 0) # 0 is white
for l in lines:
    coords = (0,0)
    for d in l:
        coords = apply(coords, mappings[d])
    tile_colours[coords] = 1 ^ tile_colours[coords]

print('part 1')
print(sum(list(tile_colours.values())))

print('part 2')
def new_colour(coords, tile_colours):
    colour = tile_colours[coords]
    neighbour_coords = [apply(coords, shift) for shift in mappings.values()]
    # n = number of black neighbouring tiles
    n = sum([tile_colours[c] for c in neighbour_coords if c in tile_colours])
    if colour == 1 and (n == 0 or n > 2):
        return 0
    if colour == 0 and n == 2:
        return 1
    return colour

def simulate(tile_colours):
    new_tile_colours = defaultdict(lambda: 0)
    for coords in tile_colours:
        new_tile_colours[coords] = new_colour(coords, tile_colours)
    assert len(tile_colours.keys()) == len(new_tile_colours.keys())
    return new_tile_colours

for i in range(100):
    for coords in list(tile_colours.keys()):
        neighbour_coords = [apply(coords, shift) for shift in mappings.values()]
        for c in neighbour_coords:
            if c not in tile_colours:
                tile_colours[c] = 0
    tile_colours = simulate(tile_colours)

print(sum(list(tile_colours.values())))
