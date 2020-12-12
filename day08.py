#!/usr/bin/env python3

instructions = [l for l in open('2020day08input').readlines()]

def computer(instructions, swap=-1):
    accumulator = 0
    i = 0
    seen = set()
    while i < len(instructions):
        if i in seen:
            return 1, accumulator
        seen.add(i)
        op, arg = instructions[i].split()
        if swap == i and op != 'acc':
            op = 'jmp' if op == 'nop' else 'nop'
        if op == 'acc':
            accumulator += int(arg)
            i += 1
        elif op == 'nop':
            i += 1
        elif op == 'jmp':
            i += int(arg)
        else:
            print("this shouldn't happen")
    return 0, accumulator

print(f'part 1: {computer(instructions)[1]}')

jmps_and_nops = [i for i,instruction in enumerate(instructions) if 'acc' not in instruction]
for i in jmps_and_nops:
    exitstatus, result = computer(instructions, swap=i)
    if not exitstatus:
        print(f'part 2: {result}')
        break
