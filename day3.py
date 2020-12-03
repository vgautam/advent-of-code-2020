from functools import partial
map_grid = []

with open('2020day3input', 'r', encoding='utf-8') as fo:
    for line in fo:
        map_grid.append([c for c in line.strip()])
map_height = len(map_grid)
map_width = len(map_grid[0])
#print(map_height, map_width)

print('part 1')
def get_num_trees(slope, map_grid):
    starting_coords = (0,0)
    num_trees = 0
    coords = starting_coords
    while True:
        updated_coords = (coords[0] + slope[0], coords[1] + slope[1])
        # the map repeats endlessly, so do like a circular array thing
        coords = (updated_coords[0], updated_coords[1] % map_width)
        #print(coords)
        if coords[0] >= len(map_grid):
            break
        #print(map_grid[coords[0]][coords[1]])
        if map_grid[coords[0]][coords[1]] == '#':
            num_trees += 1
    return num_trees
print(get_num_trees((1,3), map_grid))

print('part 2')
slopes = [(1,1), (1,3), (1,5), (1,7), (2,1)]
get_num_trees_partial = partial(get_num_trees, map_grid=map_grid)
# there's probably a better way to do this
product = 1
for x in map(get_num_trees_partial, slopes):
    product *= x
print(product)
