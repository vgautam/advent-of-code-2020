#!/usr/bin/env python3
from functools import reduce
from math import gcd

day=13 # update me
inp_f = f'2020day{day:02d}input'
#inp_f = 'test13'

earliest_time = int(open(inp_f).readline())
buses = [int(bus) for bus in open(inp_f).readlines()[1].strip().split(',') if bus != 'x']

departure = {}
for bus in buses:
    departure[bus] = earliest_time - (earliest_time % bus) + bus

bus = min(departure, key=departure.get)
print('part1:', bus*(departure[bus]-earliest_time))

buses = [bus for bus in open(inp_f).readlines()[1].strip().split(',')]

def get_multiplicative_inverse(tup):
    Ni, n = tup
    #print(f'i wanna simplify and solve this congruence: {Ni}*x_i is congruent to 1 mod {n}')
    simplified =  Ni - ((Ni // n) * n)
    x_i = 1
    while True:
        if simplified*x_i % n == 1:
            return x_i
        x_i += 1

pos_bus_tups = [(0, int(buses[0]))]
for i,b in enumerate(buses):
    if b != 'x' and i != 0:
        pos_bus_tups.append(((int(b)-i)%int(b), int(b)))
positions = [tup[0] for tup in pos_bus_tups]
buses = [tup[1] for tup in pos_bus_tups]
bs = positions
ns = buses 
N = reduce(lambda a,b: a*b, ns)
Nis = list(map(lambda n: int(N/n), buses))
xis = list(map(get_multiplicative_inverse, zip(Nis, ns)))
bNixis = [bs[i] * Nis[i] * xis[i] for i in range(len(bs))]
for i,bNixi in enumerate(bNixis):
    assert bNixi % ns[i] == bs[i], (i, bs[i], ns[i], bNixi)
x = sum(bNixis) % N
print(f'part2: {x}')
