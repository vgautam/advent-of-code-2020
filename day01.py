#!/usr/bin/env python3

numbers = []
with open('2020day1input', 'r', encoding='utf-8') as fo:
    for line in fo:
        numbers.append(int(line.strip()))

print('part 1')
for i in numbers:
    for j in numbers:
        if i + j == 2020:
            print(i*j)

print('part 2')
for i in numbers:
    for j in numbers:
        for k in numbers:
            if i + j + k == 2020:
                print(i*j*k)
