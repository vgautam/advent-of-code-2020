#!/usr/bin/env python3

# is all this code ugly? yes
# can i do better? also yes

day=23 # update me
inp_f = f'2020day{day:02d}input'

lines = [int(c) for c in open(inp_f).read().strip()]
#lines = [int(c) for c in '389125467']

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    def __str__(self):
        return str(self.val)

def initialize(lines):
    node_mapping = [None] * (len(lines)+1)
    first_node = Node(lines[0])
    node_mapping[lines[0]] = first_node
    prev_node = first_node
    for c in lines[1:]:
        new_node = Node(c)
        node_mapping[c] = new_node
        prev_node.next = new_node
        prev_node = new_node
    prev_node.next = first_node
    return node_mapping, first_node

# gotta love generators for cool shit like this <3
# also i realized i am not as comfortable with generators as i probably should be
def traverse(curr_node):
    while True:
        yield curr_node
        curr_node = curr_node.next

print('part 1')
def crab_game(num_moves, _min, _max, first_node):
    i = 0
    t = traverse(first_node)
    for iteration in range(num_moves):
        cup = next(t)
        cup_val = cup.val
        replace = cup.val - 1
        displaced_cups = []
        displaced_cup_vals = []
        for _ in range(3):
            d_c = next(t)
            displaced_cups.append(d_c)
            displaced_cup_vals.append(d_c.val)
        if replace < _min:
            replace = _max
        while replace in displaced_cup_vals:
            replace -= 1
            if replace < _min:
                replace = _max
        assert replace >= _min
        replace_node = node_mapping[replace]
        # update pointers
        cup.next = displaced_cups[-1].next
        t = traverse(curr_node=cup.next)
        displaced_cups[-1].next = replace_node.next
        replace_node.next = displaced_cups[0]
        assert replace == replace_node.val

_min = min(lines)
_max = max(lines)
node_mapping, first_node = initialize(lines)
crab_game(100, _min, _max, first_node)

answer = ''
node = node_mapping[1].next
t = traverse(node.next)
while node.val != 1:
    answer += str(node)
    node = next(t)
print(answer)

print('part 2')
for i in range(_max+1,1000001):
    lines.append(i)
_min = min(lines)
_max = max(lines)
node_mapping, first_node = initialize(lines)
crab_game(10000000, _min, _max, first_node)
node = node_mapping[1].next
t = traverse(node)
print(next(t).val * next(t).val)
