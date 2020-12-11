#!/usr/bin/env python3

#lines = open('2020day11input').read().split() # every word
#lines = open('2020day11input').readlines() # every line + \n
#lines = [l.strip() for l in open('2020day11input')] # every line
#lines = [l.strip() for l in open('2020day11input').read().split('\n\n')] # every block separated by 2 newlines
#lines = [l.split() for l in open('2020day11input').read().split('\n\n')] # every block separated by 2 newlines, split into words
grid = [[c for c in l.strip()] for l in open('2020day11input')] # every block separated by 2 newlines, split into words
#grid = [[c for c in l.strip()] for l in open('test')] # every block separated by 2 newlines, split into words

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

def valid_row(row):
    if row < 0 or row >= height:
        return False
    return True

def valid_col(col):
    if col < 0 or col >= width:
        return False
    return True

def get_adjacent_seen_in1dir(grid, row, col, direction_tup):
    prev_row = row
    prev_col = col
    while True:
        new_row = prev_row + direction_tup[0]
        new_col = prev_col + direction_tup[1]
        if not (valid_row(new_row) and valid_col(new_col)):
            return
        next_seat = (new_row, new_col)
        if grid[next_seat[0]][next_seat[1]] != '.':
            return grid[next_seat[0]][next_seat[1]]
        prev_row = new_row
        prev_col = new_col

def get_adjacent_seen(grid, seat_tup):
    adjacent_seats = []
    row = seat_tup[0]
    col = seat_tup[1]
    directions = [(-1,-1), (-1,0), (-1,+1),
                  (0,-1), (0,+1),
                  (1,-1), (1,0), (1,+1)]
    for direction in directions:
        next_seat = get_adjacent_seen_in1dir(grid, row, col, direction)
        if next_seat:
            adjacent_seats.append(next_seat)
    assert len(adjacent_seats) >= 3
    return adjacent_seats

def update_seat(adj_seats, seat, threshold=4):
    if seat != '.':
        occ_count = adj_seats.count('#')
        if occ_count == 0:
            return '#'
        if occ_count >= threshold:
            return 'L'
    return seat

#print(update_seat(['.', 'L', 'L'], '#'))

def update_round(grid, adjacent=True, threshold=4):
    # each round is independent
    new_grid = []
    for i,row in enumerate(grid):
        new_row = []
        for j,seat in enumerate(row):
            if adjacent:
                adj_seats = get_adjacent(grid, get_adjacent_positions((i,j)))
            else:
                adj_seats = get_adjacent_seen(grid, (i,j))
            new_row.append(update_seat(adj_seats, seat, threshold=threshold))
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
        
print('part 1')
answer = part1(grid)
print(sum([row.count('#') for row in answer]))
#print(answer.count('#'))

print('part 2')
def part2(grid):
    prev_grid = grid
    while True:
#        print(prev_grid)
        new_grid = update_round(prev_grid, adjacent=False, threshold=5)
        if new_grid == prev_grid:
            return new_grid
        prev_grid = new_grid

answer = part2(grid)
print(sum([row.count('#') for row in answer]))
#print(answer.count('#'))
