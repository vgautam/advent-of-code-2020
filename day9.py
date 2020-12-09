#!/usr/bin/env python3

from itertools import chain, combinations

lines = [int(l) for l in open('2020day9input').read().split()] # every word
#lines = [int(l) for l in open('test').read().split()] # every word
#lines = open('2020day9input').readlines() # every line + \n
#lines = [l.strip() for l in open('2020day9input')] # every line
#lines = [l.strip() for l in open('2020day9input').read().split('\n\n')] # every block separated by 2 newlines
#lines = [l.split() for l in open('2020day9input').read().split('\n\n')] # every block separated by 2 newlines, split into words

print('part 1')
def possible_sum(options, _sum):
    print(options, _sum)
    for i in range(len(options)):
        for j in range(len(options)):
            #print(i, j)
            if i != j and options[i] + options[j] == _sum:
                return True
    return False

#print(lines)
#print(len(lines))
stepsize = 25
for i in range(stepsize, len(lines), 1):
    print(i)
    if not possible_sum(lines[i-stepsize:i], lines[i]):
        print(lines[i])
        break


print('part 2')

def powerset(iterable):
    s = list(iterable)
    length = len(s)
    for i in range(length):
        for j in range(length):
            yield s[i:j+1]

def contiguous_sum(options, _sum):
    if sum(options) == _sum:
        return True
    return False

#print(powerset(lines[:534]))
for i in powerset(lines[:534]):
    if contiguous_sum(i, 36845998):
        print(i)
        break

print(min(i) + max(i))
