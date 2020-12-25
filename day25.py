#!/usr/bin/env python3

day=25 # update me
inp_f = f'2020day{day:02d}input'

lines = [int(c) for c in open(inp_f).read().split()] # every word
card_pubkey = lines[0]
#card_pubkey = 5764801
door_pubkey = lines[1]
#door_pubkey = 17807724

def get_loop_num(pubkey, subj_num):
    val = 1
    i = 0
    while val != pubkey:
        val = val * subj_num
        val = val % 20201227
        i += 1
    return i

def encrypt(subj_num, loop_size):
    val = 1
    for _ in range(loop_size):
        val = val * subj_num
        val = val % 20201227
    return val

print('part 1')
door_loopnum = get_loop_num(door_pubkey, 7)
card_loopnum = get_loop_num(card_pubkey, 7)
print(encrypt(door_pubkey, card_loopnum))

print('part 2')
