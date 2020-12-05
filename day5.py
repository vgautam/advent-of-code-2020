from math import ceil

row_col_dirs = []
with open('2020day5input', 'r', encoding='utf-8') as fo:
#with open('sample', 'r', encoding='utf-8') as fo:
    for line in fo:
        l = line.strip()
        row_col_dirs.append((l[:7], l[7:]))

#print(row_cols)

def split(options, direction):
    if direction == 'down':
        return options[:ceil(len(options)/2)]
    return options[ceil(len(options)/2):]

def translate_direction(string):
    if string == 'F': return 'down'
    elif string == 'B': return 'up'
    elif string == 'R': return 'up'
    elif string == 'L': return 'down'
    raise ValueError

def binary_search(options, directions):
    directions = [translate_direction(c) for c in directions]
    for direction in directions:
        #print(options, direction)
        options = split(options, direction)
    assert len(options) == 1
    return options[0]

def get_seat_id(row, column):
    return row * 8 + column

print('part 1')
rows = list(range(128))
columns = list(range(8))
seat_ids = []
for row_dirs, col_dirs in row_col_dirs:
    #print(row_dirs, col_dirs)
    row = binary_search(rows, row_dirs)
    col = binary_search(columns, col_dirs)
    seat_id = get_seat_id(row, col)
    #print(row, col, seat_id)
    seat_ids.append(seat_id)
print(max(seat_ids))

print('part 2')
