#!/usr/bin/env python3

day=22 # update me
inp_f = f'2020day{day:02d}input'
#inp_f = 'test22'

#lines = open(inp_f).read().split() # every word
#lines = open(inp_f).readlines() # every line + \n
#lines = [l.strip() for l in open(inp_f)] # every line
#lines = [l.strip() for l in open(inp_f).read().split('\n\n')] # every block separated by 2 newlines
lines = [l.split()[2:] for l in open(inp_f).read().split('\n\n')] # every block separated by 2 newlines, split into words

player1 = [int(x) for x in lines[0]]
player2 = [int(x) for x in lines[1]]
print('part 1')
while len(player1) != 0 and len(player2) != 0:
    play1 = player1.pop(0)
    play2 = player2.pop(0)
    if play1 > play2:
        player1 += [play1, play2]
        winner = player1
    elif play2 > play1:
        player2 += [play2, play1]
        winner = player2

winner.reverse()
print(sum([x*(i+1) for i,x in enumerate(winner)]))

print('part 2')
