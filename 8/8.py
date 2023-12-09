from statistics import mode, StatisticsError
from math import lcm

with open('input.txt', 'r+') as f:
    data = [line.strip('\n') for line in f.readlines()]
print("Day 8")

directions = [1 if d=='R' else 0 for d in data[0]]
next_node = {line[:line.index('=')-1] : (line[line.index('(')+1:line.index(',')],
                                         line[line.index(',')+2:line.index(')')]) for line in data[2:]}

def part1():
    current = 'AAA'
    steps = 0
    while current != 'ZZZ':
        current = next_node[current][directions[steps%len(directions)]]
        steps += 1
    return(steps)
print("Part 1:", part1())

ghosts = [x for x in next_node.keys() if x[-1]=='A']

offsets = []
periods = []

for g in ghosts:
    steps = 0
    current = g
    while current[-1] != 'Z':
        current = next_node[current][directions[steps%len(directions)]]
        steps += 1
    offsets.append(steps)
    current = next_node[current][directions[steps%len(directions)]]
    steps += 1
    while current[-1] != 'Z':
        current = next_node[current][directions[steps%len(directions)]]
        steps += 1
    periods.append(steps-offsets[-1])

if offsets == periods: # This shouldn't really work, but it was worth trying and it does, so...
    print("Part2:", lcm(*offsets))
