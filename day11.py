#!/usr/bin/env python3

#lines = open('2020day11input').read().split() # every word
#lines = open('2020day11input').readlines() # every line + \n
#lines = [l.strip() for l in open('2020day11input')] # every line
#lines = [l.strip() for l in open('2020day11input').read().split('\n\n')] # every block separated by 2 newlines
#lines = [l.split() for l in open('2020day11input').read().split('\n\n')] # every block separated by 2 newlines, split into words
grid = [[c for c in l.strip()] for l in open('2020day11input')] # every block separated by 2 newlines, split into words
grid = [[c for c in l.strip()] for l in open('test')] # every block separated by 2 newlines, split into words

height = len(grid)
width = len(grid[0])
print(height, width)

def get_adjacent_positions(seat_tup):
    adj_pos = []
    adj_pos.append((seat_tup[0]-1, seat_tup[1]-1))
    adj_pos.append((seat_tup[0]-1, seat_tup[1]))
    adj_pos.append((seat_tup[0]-1, seat_tup[1]+1))
    adj_pos.append((seat_tup[0], seat_tup[1]-1))
    adj_pos.append((seat_tup[0], seat_tup[1]+1))
    adj_pos.append((seat_tup[0]+1, seat_tup[1]-1))
    adj_pos.append((seat_tup[0]+1, seat_tup[1]))
    adj_pos.append((seat_tup[0]+1, seat_tup[1]+1))
    assert len(adj_pos) == 8
    return adj_pos

#print(get_adjacent_positions((0,0)))

def get_adjacent(grid, adj_positions):
    adjacent_seats = []
    for pos in adj_positions:
        row = pos[0]
        col = pos[1]
        if row < 0 or row >= height:
#            print('bad row', row)
            continue
        if col < 0 or col >= width:
#            print('bad col', col)
            continue
        adjacent_seats.append(grid[row][col])
    assert len(adjacent_seats) >= 3
    return adjacent_seats

#print(get_adjacent(grid, get_adjacent_positions((0,0))))

def update_seat(adj_seats, seat):
    if seat != '.':
        occ_count = adj_seats.count('#')
        if occ_count == 0:
            return '#'
        if occ_count >= 4:
            return 'L'
    return seat

#print(update_seat(['.', 'L', 'L'], '#'))

def update_round(grid):
    # each round is independent
    new_grid = []
    for i,row in enumerate(grid):
        new_row = []
        for j,seat in enumerate(row):
            adj_seats = get_adjacent(grid, get_adjacent_positions((i,j)))
            new_row.append(update_seat(adj_seats, seat))
        new_grid.append(new_row)
    return new_grid

def part1(grid):
    prev_grid = grid
    while True:
#        print(prev_grid)
        new_grid = update_round(prev_grid)
        if new_grid == prev_grid:
            return new_grid
        prev_grid = new_grid
        
answer = part1(grid)
print(sum([row.count('#') for row in answer]))
#print(answer.count('#'))

print('part 1')

print('part 2')
