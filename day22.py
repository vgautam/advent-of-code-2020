#!/usr/bin/env python3

day=22 # update me
inp_f = f'2020day{day:02d}input'
#inp_f = 'test22'

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
# pretty slow but watcha gonna do
player1 = [int(x) for x in lines[0]]
player2 = [int(x) for x in lines[1]]
def recursive_combat(player1, player2):
    previously_seen_configurations = []
    while len(player1) != 0 and len(player2) != 0:
        configuration = ';'.join([','.join([str(x) for x in player1]), ','.join([str(x) for x in player2])])
        if configuration in previously_seen_configurations:
            winner = (1, player1)
            return winner
        previously_seen_configurations.append(configuration)
        play1 = player1.pop(0)
        play2 = player2.pop(0)
        if len(player1) >= play1 and len(player2) >= play2:
            winner = recursive_combat(player1[:play1], player2[:play2])
        else:
            if play1 > play2:
                winner = (1, player1)
            elif play2 > play1:
                winner = (2, player2)
        if winner[0] == 1:
            player1 += [play1, play2]
            winner = (1, player1)
        else:
            player2 += [play2, play1]
            winner = (2, player2)
    return winner

winner = recursive_combat(player1, player2)[1]
winner.reverse()
print(sum([x*(i+1) for i,x in enumerate(winner)]))
