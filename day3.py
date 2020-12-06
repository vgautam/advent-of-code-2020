#!/usr/bin/env python3
from functools import reduce

map_grid = [list(line.strip()) for line in open('2020day3input')]
map_height = len(map_grid)
map_width = len(map_grid[0])

def get_num_trees(slope, map_grid=map_grid):
    num_trees = 0
    coords = (0,0)
    while coords[0] < map_height-1:
        # the map repeats endlessly, so do like a circular array thing
        coords = (coords[0]+slope[0], (coords[1]+slope[1]) % map_width)
        if map_grid[coords[0]][coords[1]] == '#':
            num_trees += 1
    return num_trees

print(f'part 1: {get_num_trees((1,3))}')
print(f'part 2: {reduce(lambda a, b: a * b, map(get_num_trees, [(1,1), (1,3), (1,5), (1,7), (2,1)]))}')
