#!/usr/bin/env python3
from collections import defaultdict

day=17 # update me
inp_f = f'2020day{day:02d}input'
#inp_f = 'test'

lines = [[c for c in l] for l in open(inp_f).read().split()]

print('part 1')

def initialize_pocket(dims=3):
    pocket = defaultdict(lambda: '.')
    for x,row in enumerate(lines):
        for y,col in enumerate(row):
            coords = (x,y,0)
            if dims == 4:
                coords = (x,y,0,0) 
            pocket[coords] = col
    return pocket

def nearby_coords(coords, dims=3):
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            for z in [-1,0,1]:
                if dims == 3 and not (x == 0 and y == 0 and z == 0):
                    yield(coords[0]+x, coords[1]+y, coords[2]+z)
                if dims == 4:
                    for aa in [-1,0,1]: # ha, excel reference
                        if not (x == 0 and y == 0 and z == 0 and aa == 0):
                            yield(coords[0]+x, coords[1]+y, coords[2]+z, coords[3]+aa)
                

#print(len(list(nearby_coords((1,2,3)))))

def updated_value(state, neighbours):
    nearby_active_count = list(neighbours).count('#')
    if state == '#':
        if nearby_active_count == 2 or nearby_active_count == 3:
            return '#'
        return '.'
    if nearby_active_count == 3:
        return '#'
    return '.'


def simulate(pocket, dims=3):
    new_pocket = defaultdict(lambda: '.')
    for coords in list(pocket.keys()):
        orig_value = pocket[coords]
        neighbours = [pocket[n] for n in nearby_coords(coords, dims=dims)]
        new_pocket[coords] = updated_value(orig_value, neighbours)
    return new_pocket

pocket = initialize_pocket()
for i in range(6):
    for coords in [k for k in pocket]:
        for n in nearby_coords(coords):
            if n not in pocket:
                pocket[n] = '.'
    pocket = simulate(pocket)

print(list(pocket.values()).count('#'))

print('part 2')

pocket = initialize_pocket(dims=4)
for i in range(6):
    for coords in [k for k in pocket]:
        for n in nearby_coords(coords, dims=4):
            if n not in pocket:
                pocket[n] = '.'
    pocket = simulate(pocket, dims=4)

print(list(pocket.values()).count('#'))
