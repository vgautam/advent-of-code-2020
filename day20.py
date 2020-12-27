#!/usr/bin/env python3
from itertools import product
from itertools import combinations
from functools import reduce
from collections import defaultdict
import numpy as np
from math import sqrt
import re

day=20 # update me
inp_f = f'2020day{day:02d}input'
inp_f = 'test'

#   0
# 3 [] 1
#   2
op_types = set(product(['r1', 'r2', 'r3'], ['vf', 'hf'])) | set(product(['vf', 'hf'], ['r1', 'r2', 'r3'])) | {('vf',), ('hf',), ('r1',), ('r2',), ('r3',)}

def modify(tile, ops):
    new_tile = [t for t in tile]
    for op in ops:
        if 'r' in op:
            for i in range(int(op.split('r')[1])):
                new_tile = [''.join(t) for t in np.rot90([list(t) for t in new_tile])]
        elif op == 'vf':
            new_tile =  [t for t in new_tile[::-1]]
        elif op == 'hf':
            new_tile = [t[::-1] for t in new_tile]
    return new_tile

def get_edges(tile):
    return [tile[0],
            ''.join([r[-1] for r in tile[0:]]),
            tile[-1],
            ''.join([r[0] for r in tile[0:]])]

tiles_raw = [l.split() for l in open(inp_f).read().split('\n\n')]
tiles = {}
for t in tiles_raw:
    tile_id = t[1].split(':')[0]
    tile = t[2:]
    tiles[tile_id] = [tile]
    for ops in op_types:
        alt_tile = modify(tile, ops)
        if alt_tile not in tiles[tile_id]:
            tiles[tile_id].append(alt_tile)

# If I started with a sensible tile edge convention, I could probably have avoided this
def opp_edge(i):
    mapping = {1: 3, 0: 2, 2: 0, 3: 1}
    return mapping[i]

def create_map():
    gigantic_map = {}
    for tile in tiles:
        for o_num, orientation in enumerate(tiles[tile]):
            edges = get_edges(orientation)
            orientation_map = {}
            for other_tile in set(tiles.keys())-{tile}:
                for other_orientation in tiles[other_tile]:
                    other_edges = get_edges(other_orientation)
                    for i,edge in enumerate(edges):
                        if other_edges[opp_edge(i)] == edge:
                            orientation_map[i] = (other_tile, other_orientation)
            gigantic_map[(tile, o_num)] = orientation_map
    return gigantic_map

gigantic_map = create_map()
#print(gigantic_map)

corners = []
for tile in tiles:
    # unclear if it's necessary to check every orientation, but i'm doing it to be safe
    for o_num in range(len(tiles[tile])):
        if len(gigantic_map[(tile, o_num)]) == 2:
            corners.append(tile)
print(reduce(lambda a,b: int(a)*int(b), list(set(corners))))

img_ht = int(sqrt(len(tiles)))
rowlen = 10
image_tiles = [[None for i in range(img_ht)] for j in range(img_ht)]
image_raw = [[None for i in range(img_ht)] for j in range(img_ht)]

tile_id = corners[0] # entirely arbitrary choice
for o_num in range(len(tiles[tile_id])):
    matching_edges = [k for k,v in gigantic_map[(tile_id, o_num)].items()]
    # not so arbitrary, given that i'm starting the map with this
    if matching_edges == [1,2]:
        tile = tiles[tile_id][o_num]
        tile_id = (tile_id, o_num)
        break

# yes, i could generator this but i don't want to for reasons
def get_valid_neighbour_coords(image_raw, coords):
    candidates = [(coords[0]-1,coords[1]),
                  (coords[0],coords[1]+1),
                  (coords[0]+1,coords[1]),
                  (coords[0],coords[1]-1)]
    valid = []
    for x,y in candidates:
        if x >= 0 and y >= 0 and x < len(image_raw) and y < len(image_raw):
            valid.append((x,y))
        else:
            valid.append(None)
    return valid

print('valid', get_valid_neighbour_coords(image_raw, (0,0)))
print('valid', get_valid_neighbour_coords(image_raw, (1,0)))

def get_current_neighbours(image_raw, coords):
    neighbours = [None, None, None, None]
    for i,c in enumerate(get_valid_neighbour_coords(image_raw, coords)):
        if c is not None:
            (x,y) = c
            neighbours[i] = image_raw[x][y]
    return neighbours

def get_missing_positions(image_raw, coords):
    return [i for i,pos in enumerate(get_valid_neighbour_coords(image_raw, coords)) if pos is not None and image_raw[pos[0]][pos[1]] is None]

def get_neighbours_from_edge_map(edge_map):
    neighbours = [None, None, None, None]
    for direction, neighbour in edge_map.items():
        if neighbour != None:
            neighbour_tile_id, neighbour_tile = neighbour
            neighbours[direction] = (neighbour_tile_id, neighbour_tile)
    return neighbours

# constraints of the form [None, <some-orientation>, <other-orientation>, None], etc.
def get_all_neighbours(orientations, constraints, options, missing):
    valid_os = [i for i in orientations]
    neighbours = []
    for tile_id, o_num in orientations:
        edge_map = gigantic_map[(tile_id, o_num)]
        matching_edges = {k: v[1] for k,v in edge_map.items()}
        for i,constraint in enumerate(constraints):
            # this lets me treat borders as constraints
            if constraint is None:
                continue
            if i not in matching_edges or matching_edges[i] != constraint:
                valid_os.remove(o_num)
                break
        for i in missing:
            # need to find something here that fits
            if i not in matching_edges and o_num in valid_os:
                valid_os.remove(o_num)
    assert valid_os
    return valid_os[0], get_neighbours_from_edge_map(gigantic_map[valid_os[0]])

def print_image(image_raw):
    image = []
    for row_raw in image_raw:
        row = []
        for t_raw in row_raw:
            if t_raw:
                row.append(t_raw)
            else:
                row.append(['?'*rowlen for _ in range(rowlen)])
        image.append(row)
    pic = []
    for row in image:
        curr_row = ''
        for i in range(len(row[0])):
            for tile in row:
                curr_row += ''.join([tile[i]])
                curr_row += ' '
            curr_row += '\n'
        pic.append(curr_row)
    print('\n'.join(pic))

# horrible, hacky, this file is slowly getting nasty again
def get_tile_onum(tile_id, tile):
    for o_num,_tile in enumerate(tiles[tile_id]):
        if tile == _tile:
            return o_num

def part2(image_raw, image_tiles, tile_ident, tile):
    tile_id, o_num = tile_ident
    for (x,y) in product(range(img_ht), range(img_ht)):
        orientations = [(tile_id, o_num) for o_num in range(len(tiles[tile_id]))]
        if image_raw[x][y] is None:
            image_raw[x][y] = tile
            image_tiles[x][y] = (tile_id, o_num)
        else:
            tile = image_raw[x][y]
            tile_id, o_num = image_tiles[x][y]
        orientations = [(tile_id, o_num)]
        print_image(image_raw)
        pool = set(tiles.keys()) - {tile_id}
        constraints = get_current_neighbours(image_raw, (x,y))
        missing = get_missing_positions(image_raw, (x,y))
        (tile_id, o_num), neighbours = get_all_neighbours(orientations, constraints, pool, missing)
        image_raw[x][y] = tiles[tile_id][o_num]
        image_tiles[x][y] = (tile_id, o_num)
        neighbour_coords = get_valid_neighbour_coords(image_raw, (x,y))
        for i,m in enumerate(missing):
            if i == 0:
                x,y = neighbour_coords[m]
                tile_id, tile = neighbours[m]
            x_,y_ = neighbour_coords[m]
            tile_id_, tile_ = neighbours[m]
            image_raw[x_][y_] = tile_
            image_tiles[x_][y_] = (tile_id_, get_tile_onum(tile_id_, tile_))

part2(image_raw, image_tiles, tile_id, tile)
