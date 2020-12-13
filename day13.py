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

# Some notes for later:
# If I have [7,13] in my list of buses then to solve part 2 I need to find timestamp t (a natural number) such that
# 7 * x = t (for some natural number x), AND
# 13 * y = t + 1 (for some natural number y)
# So there's many options for x and y that would work.
# I feel like the natural number bit has to be relevant somehow.
# This is saying the same thing as
# t mod 7 == 0
# t mod 13 == 1
# but idk how to solve equations with mods.
# One thing I could potentially do is to take my current approach and parallelize it over pairs of
# numbers, e.g., if I have a list that looks like [7,x,x,x,13,x,x,x,29], then I could brute force
# the solution to [7,x,x,x,13] and [13,x,x,x,29] and then... do something with that?
# Like take the max timestamp of the partial results and re-check all of them and go up from there?
# Also why are all the numbers in my input prime. This seems highly suspicious and I'm even more
# convinced that this is some clever math thing I've never heard of

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
