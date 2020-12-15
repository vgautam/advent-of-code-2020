#!/usr/bin/env python3
import re

day=14 # update me
inp_f = f'2020day{day:02d}input'
#inp_f = 'test'

memory = {} # all alone in the moonlight

print('part 1')
for line in open(inp_f):
   if line.startswith('mask'):
       mask_raw = line.split('mask = ')[1]
       mask_and = int(line.split('mask = ')[1].replace('X', '1'), 2)
       mask_or = int(line.split('mask = ')[1].replace('X', '0'), 2)
   else:
       address = line.split(']')[0][4:]
       value = int(bin(int(line.split()[-1])),2)
       #print(f'write {(mask_and & value) | mask_or} to {address}')
       memory[address] = (mask_and & value) | mask_or

print(sum(memory.values()))

print('part 2')
memory = {}
# ok having thought about it for a long time i think i need to just use the strings as strings
for line in open(inp_f):
   if line.startswith('mask'):
       mask_raw = line.split('mask = ')[1].strip()
       assert len(mask_raw) == 36
   else:
       address = f"{int(line.split(']')[0][4:]):0>36b}"
       value = int(line.split()[-1])
       assert len(address) == 36
       address_range = ''
       x_locations = []
       for i,c in enumerate(address):
           if mask_raw[i] == '0':
               address_range += c
           elif mask_raw[i] == 'X':
               x_locations.append(i)
               address_range += mask_raw[i]
           else:
               address_range += mask_raw[i]
       num_possibilities = 2 ** address_range.count('X')
       for num in range(num_possibilities):
           x_values = f'{num:b}'.zfill(len(x_locations))
           address = ''
           for i,c in enumerate(address_range):
               if i in x_locations:
                  address += x_values[x_locations.index(i)]
               else:
                  address += c
           #print(int(address, 2))
           memory[address] = value

print(sum(memory.values()))
