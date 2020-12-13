#!/usr/bin/env python3

day=13 # update me
inp_f = f'2020day{day:02d}input'
#inp_f = 'test'

earliest_time = int(open(inp_f).readline())
buses = [int(bus) for bus in open(inp_f).readlines()[1].strip().split(',') if bus != 'x']

departure = {}
for bus in buses:
    departure[bus] = earliest_time - (earliest_time % bus) + bus

bus = min(departure, key=departure.get)
print('part1:', bus*(departure[bus]-earliest_time))

print('part 2')
