#!/usr/bin/env python3
from functools import reduce

day=13 # update me
inp_f = f'2020day{day:02d}input'
inp_f = 'test'

earliest_time = int(open(inp_f).readline())
buses = [int(bus) for bus in open(inp_f).readlines()[1].strip().split(',') if bus != 'x']

departure = {}
for bus in buses:
    departure[bus] = earliest_time - (earliest_time % bus) + bus

bus = min(departure, key=departure.get)
print('part1:', bus*(departure[bus]-earliest_time))

buses = [bus for bus in open(inp_f).readlines()[1].strip().split(',')]

# solve for t
def departs_at(bus, timestamp):
    result = bus == 'x' or timestamp % int(bus) == 0
    return result

first_bus = int(buses[0])
divisor = 1
#divisor = 100000000000000 // first_bus
while True:
    t = first_bus * divisor
    found = True
    for i, bus in enumerate(buses[1:]):
        if not departs_at(bus, t+i+1):
            found = False
            break
    if found:
        break
    divisor += 1

print('part2:', t)
