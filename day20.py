#!/usr/bin/env python3
from itertools import product
from collections import defaultdict

day=20 # update me
inp_f = f'2020day{day:02d}input'
inp_f = 'test'

# putting down some ideas before i actually try this out tomorrow
# - the tile insides don't matter, so just work with the borders after reading them in
# - this could be really fast by converting to binary and doing bitwise ops, e.g., if a xor b == 0b0 then it's a match
# - instead of brute forcing every combination of tiles, use dicts: edges (in binary) as keys,
#   tile IDs as vals
# - after that it'll be kinda like constraint matching from day whatever it was?
# but wait, what data structure will hold the WIP image? it's like a puzzle
# there might be gaps where it's relevant to know the edges from the 4 surrounding tiles
# a matrix of 4-tuples, representing tiles (1 val for each of 4 edges)?
# but when starting to build it you wouldn't know where a tile goes exactly, so you'd have to be
# able to move stuff around. Or do something vaguely linkedlisty like each tile edge is ({binary-representation-of-edge}, {next-tile-id})
# oooo! this could work

# day 2 notes
# arbitrarily defining the order of edges of a tile to be top down left right
# okay, this is gnarly as fuck
# every valid candidate tile (whatever flip/rotate combo) must match other tiles on exactly 2, 3
# or 4 sides (depending on whether it's an edge, corner or middle tile
# Could I prune out some flip/rotate combos using this? would it even help?

op_types = set(product(['r1', 'r2', 'r3'], ['vf', 'hf'])) | set(product(['vf', 'hf'], ['r1', 'r2', 'r3'])) | {('vf',), ('hf',), ('r1',), ('r2',), ('r3',)}
print(op_types)
print(len(op_types))

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
seen_dict = defaultdict(set)
for t in tiles_raw:
    tile_id = t[1].split(':')[0]
    edge1 = t[2]
    edge2 = t[-1]
    edge3 = ''.join([r[0] for r in t[2:]])
    edge4 = ''.join([r[-1] for r in t[2:]])
    edges = [edge1, edge2, edge3, edge4]
    edges = [e.replace('#', '1').replace('.', '0') for e in edges]
    tiles[tile_id] = [edges, []]
    for ops in op_types:
        alt_tile = modify(edges, ops)
        for e in alt_tile:
            suffix = '_' + '_'.join(ops) if ops else ''
            seen_dict[e].add(tile_id + suffix)
    print(tile_id, edges)
    assert edges == hflip(hflip(edges))
    assert edges == vflip(vflip(edges))
    assert edges == rotate(rotate(rotate(rotate(edges))))

def get_smolest_resolvable_case(seen_dict, max_tiles=1):
    subset_dict = defaultdict(set)
    for k in seen_dict:
        unique_tiles = {v.split('_')[0] for v in seen_dict[k]}
        if len(unique_tiles) == max_tiles:
            subset_dict[k] = seen_dict[k]
    return subset_dict

#print([(k,v) for k,v in seen_dict.items() if len(v) == 7])
print(get_smolest_resolvable_case(seen_dict, 2))
print(len(get_smolest_resolvable_case(seen_dict, 2)))

print('part 1')

print('part 2')
