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
print(sum([1 for t in tile_colours if tile_colours[t] == 1]))

print('part 2')
