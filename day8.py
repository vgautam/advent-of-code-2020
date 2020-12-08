#!/usr/bin/env python3

instructions = []
with open('2020day8input', 'r', encoding='utf-8') as fo:
    for line in fo:
        instructions.append(line.split())

#print(instructions)
def computer(instructions):
    acc = 0
    i = 0
    seen = set()
    while i < len(instructions):
        #print(i, len(instructions))
        if i in seen:
            #print('bad', acc)
            return 1, acc
        seen.add(i)
        #print(i)
        if instructions[i][0] == 'acc':
            acc += int(instructions[i][1])
            i += 1
            continue
        if instructions[i][0] == 'nop':
            i+= 1
            continue
        if instructions[i][0] == 'jmp':
            i+= int(instructions[i][1])
    return 0, acc

def swap(instruction):
    if instruction[0] == 'jmp':
        return ['nop', instruction[1]]
    elif instruction[0] == 'nop':
        return ['jmp', instruction[1]]
    return instruction

print('part 1')
print(computer(instructions))

instructions = []
with open('2020day8input', 'r', encoding='utf-8') as fo:
#with open('test', 'r', encoding='utf-8') as fo:
    for line in fo:
        instructions.append(line.split())

print('part 2')
for j in range(len(instructions)):
    #print(j)
    #print(instructions)
    new_instructions = [i for i in instructions]
    new_instructions[j] = swap(new_instructions[j])
    exitstatus, result = computer(new_instructions)
    if not exitstatus:
        print(result)
    #print(exitstatus, result)
