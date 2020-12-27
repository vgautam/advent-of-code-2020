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

#   1
# 4 [] 2
#   3
def get_edges(tile):
    yield tile[0]
    yield ''.join([r[-1] for r in tile[0:]])
    yield tile[-1]
    yield ''.join([r[0] for r in tile[0:]])

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

def get_tiles(tiles, num_matching):
    candidate_corners = {}
    for corner in tiles:
        available_tiles = tiles.keys() - {corner}
        good_orientations = []
        # diff orientations of the candidate corner tile
        for i,edges in enumerate(tiles[corner]):
            matched_edges = {}
            for other_tile in available_tiles:
                for orientation in tiles[other_tile]:
                    for x in get_edges(edges):
                        if x in get_edges(orientation):
                            matched_edges[x] = other_tile
                            break
                if len(matched_edges) > num_matching:
                    break
            if len(matched_edges) == num_matching and len(set(matched_edges.values())) == num_matching:
                good_orientations.append(edges)
            if len(good_orientations) < i:
                break
        if len(good_orientations) == len(tiles[corner]):
            candidate_corners[corner] = matched_edges.values()
    return candidate_corners

print('part 1')
candidate_corners = get_tiles(tiles, 2)
candidate_borders = get_tiles(tiles, 3)
print(reduce(lambda a,b: int(a)*int(b), candidate_corners))

#   0
# 3 [] 1
#   2
def get_neighbours(tiles, orientations, pool, missing_neighbours):
    res = []
    for orientation in orientations:
        orientation_neighbours = [None, None, None, None]
        for other_tile in pool:
            for o_i,other_orientation in enumerate(tiles[other_tile]):
                for i,x in enumerate(get_edges(orientation)):
                    if x in get_edges(other_orientation):
                        orientation_neighbours[i] = (other_tile, other_orientation)
        found_neighbours = [i for i,c in enumerate(orientation_neighbours) if c is not None]
        neighbour_tiles = [x[0] for x in orientation_neighbours if x]
        assert len(neighbour_tiles) == len(set(neighbour_tiles))
        print(missing_neighbours, found_neighbours)
        if [i for i in missing_neighbours if i in found_neighbours] == missing_neighbours:
            res.append((orientation, orientation_neighbours))
    return res

def get_neighbour_coords(coords, direction=None):
    mapping = [(coords[0]-1,coords[1]),
               (coords[0],coords[1]+1),
               (coords[0]+1,coords[1]),
               (coords[0],coords[1]-1)]
    if direction:
        return mapping[direction]
    return mapping

def valid(image_raw, coords):
    return coords[0] >= 0 and coords[1] >= 0 and coords[1] < len(image_raw) and coords[0] < len(image_raw)

def get_missing_neighbours(image_raw, coords):
    missing = []
    for i, (x,y) in enumerate(get_neighbour_coords(coords)):
        if valid(image_raw, (x,y)) and image_raw[x][y] is None:
            missing.append(i)
    return missing

img_ht = int(sqrt(len(tiles)))
image_tiles = [[None for i in range(img_ht)] for j in range(img_ht)]
image_raw = [[None for i in range(img_ht)] for j in range(img_ht)]
tile = list(candidate_corners.keys())[0]
accounted_for = set()
for (x,y) in product(range(img_ht), range(img_ht)):
    if image_raw[x][y]:
        tile = image_tiles[x][y]
    orientations = tiles[tile]
    if image_raw[x][y]:
        orientations = [image_raw[x][y]]
    print(image_tiles)
    if len(accounted_for) == len(tiles):
        break
    accounted_for.add(tile)
    pool = set(tiles.keys()) - {tile}
    missing_neighbours = get_missing_neighbours(image_raw, (x,y))
    try:
        neighbour_opts = get_neighbours(tiles, orientations, pool, missing_neighbours)
        orientation, neighbours = neighbour_opts[0][0], neighbour_opts[0][1]
    except IndexError:
        print('ERROR')
        #print(orientations)
        #print(pool)
        #print([tiles[p] for p in pool])
        #print(missing_neighbours)
        raise IndexError
    image_raw[x][y] = orientation
    image_tiles[x][y] = tile
    # fugly, clean up later
    # 2 hrs later: This entire file is nasty. Clean it tf up (or throw it out?)
    for i,direction in enumerate(missing_neighbours):
        if i == 0:
            tile = neighbours[direction][0]
        (x_, y_) = get_neighbour_coords((x,y), direction=direction)
        image_tiles[x_][y_] = neighbours[direction][0]
        image_raw[x_][y_] = neighbours[direction][1]
        accounted_for.add(neighbours[direction][0])

image = []
for row_raw in image_raw:
    row = []
    for t_raw in row_raw:
        tile = []
        for t_row in t_raw[1:-1]: # oof, this fucking naming
            tile.append(t_row[1:-1])
        row.append(tile)
    image.append(row)

pic = []
for row in image:
    for i in range(len(row[0])):
        pic.append(''.join([tile[i] for tile in row]))

#print('\n'.join(pic))

nessie1 = '                  # '
nessie2 = '#    ##    ##    ###'
nessie3 = ' #  #  #  #  #  #   '
rowlen = len(pic[0])

pic_orientations = [pic]
for ops in op_types:
    mod = modify(pic, ops)
    if mod not in pic_orientations:
        pic_orientations.append(mod)
sep = '\n'
sep = 'B'

nessies = [nessie1, nessie2, nessie3]
nessie_regexes = []
for i in range((rowlen+1-len(nessie1))):
    nessie_regex = []
    for nessie in nessies:
        nessie_regex.append(i * '.' + nessie.replace(' ', '.') + '.' * (rowlen-len(nessie1)-i))
    nessie_regexes.append(sep.join(nessie_regex))
#print('***\n' + '\n\n'.join(nessie_regexes) + '\n***')

print()

#pic_orientations = [
#""".####...#####..#...###..
######..#..#.#.####..#.#.
#.#.#...#.###...#.##.O#..
##.O.##.OO#.#.OO.##.OOO##
#..#O.#O#.O##O..O.#O##.##
#...#.#..##.##...#..#..##
##.##.#..#.#..#..##.#.#..
#.###.##.....#...###.#...
##.####.#.#....##.#..#.#.
###...#..#....#..#...####
#..#.##...###..#.#####..#
#....#.##.#.#####....#...
#..##.##.###.....#.##..#.
##...#...###..####....##.
#.#.##...#.##.#.#.###...#
##.###.#..####...##..#...
##.###...#.##...#.##O###.
#.O##.#OO.###OO##..OOO##.
#..O#.O..O..O.#O##O##.###
##.#..##.########..#..##.
##.#####..#.#...##..#....
##....##..#.#########..##
##...#.....#..##...###.##
##..###....##.#...##.##.#""".replace('O', '#').split()]

nessie_counts = []
# oh god why did i do it this inefficiently
for pic in pic_orientations:
    num_nessies = 0
    for regex in nessie_regexes:
        p = sep.join(pic)
        #if not p.startswith('.####...#..#.##..#..###.'):
        if not p.startswith('.####...#####..#...###..'):
            continue
        compiled = re.compile(regex, flags=re.MULTILINE)
        for i in range(len(p)-len(regex)):
            if compiled.match(p):
                num_nessies += 1
            p = p[1:]
    nessie_counts.append(num_nessies)

print(max(nessie_counts))
