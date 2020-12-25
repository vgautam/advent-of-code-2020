#!/usr/bin/env python3
from itertools import product
from itertools import combinations
from functools import reduce
from collections import defaultdict

day=20 # update me
inp_f = f'2020day{day:02d}input'
inp_f = 'test'

op_types = set(product(['r1', 'r2', 'r3'], ['vf', 'hf'])) | set(product(['vf', 'hf'], ['r1', 'r2', 'r3'])) | {('vf',), ('hf',), ('r1',), ('r2',), ('r3',)}

def modify(tile, ops):
    new_tile = tile
    for op in ops:
        if 'r' in op:
            for i in range(int(op.split('r')[1])):
                new_tile = rotate(new_tile)
        elif op == 'vf':
            new_tile = vflip(tile)
        elif op == 'hf':
            new_tile = hflip(tile)
    return new_tile

def rotate(tile):
    return tile[1:] + [tile[0]]

def hflip(tile):
    return [tile[0][::-1], tile[1][::-1], tile[3], tile[2]]

def vflip(tile):
    return [tile[1], tile[0], tile[2][::-1], tile[3][::-1]]

tiles_raw = [l.split() for l in open(inp_f).read().split('\n\n')]
tiles = {}
for t in tiles_raw:
    tile_id = t[1].split(':')[0]
    edge1 = t[2]
    edge2 = t[-1]
    edge3 = ''.join([r[0] for r in t[2:]])
    edge4 = ''.join([r[-1] for r in t[2:]])
    edges = [edge1, edge2, edge3, edge4]
    edges = [e.replace('#', '1').replace('.', '0') for e in edges]
    tiles[tile_id] = [edges]
    for ops in op_types:
        alt_tile = modify(edges, ops)
        if alt_tile not in tiles[tile_id]:
            tiles[tile_id].append(alt_tile)
    assert edges == hflip(hflip(edges))
    assert edges == vflip(vflip(edges))
    assert edges == rotate(rotate(rotate(rotate(edges))))

#print(tiles)

def xor(edge_pair):
    edge1 = int(edge_pair[0], 2)
    edge2 = int(edge_pair[1], 2)
    return edge1 ^ edge2 == 0b0

for corners in combinations(tiles.keys(), 4):
    available_tiles = tiles.keys() - set(corners)
    good_corners = []
    for corner in corners:
        edges = tiles[corner][0]
        matched_edges = set()
        for other_tile in available_tiles:
            for orientation in tiles[other_tile]:
                pairs = product(edges, orientation)
                for pair in pairs:
                    if xor(pair):
                        #print(f'{corner} has a match with {other_tile} ({pair})')
                        matched_edges.add(pair)
        if len(matched_edges) == 2:
            good_corners.append(corner)
    if len(good_corners) == 4:
        print('we have a winner!')
        print(reduce(lambda a,b: int(a)*int(b), good_corners))


print('part 1')

print('part 2')
