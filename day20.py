#!/usr/bin/env python3

day=20 # update me
inp_f = f'2020day{day:02d}input'
#inp_f = 'test'

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
# ok gn room gn moon ill probably be back tomorrow at noon

#lines = open(inp_f).read().split() # every word
#lines = open(inp_f).readlines() # every line + \n
#lines = [l.strip() for l in open(inp_f)] # every line
#lines = [l.strip() for l in open(inp_f).read().split('\n\n')] # every block separated by 2 newlines
#lines = [l.split() for l in open(inp_f).read().split('\n\n')] # every block separated by 2 newlines, split into words

print(lines)

print('part 1')

print('part 2')
