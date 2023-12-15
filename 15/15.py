from functools import cache

with open('input.txt', 'r+') as f:
    data = [line.strip('\n').split(',') for line in f.readlines()][0]
print("Day 15")

def HASH(s:str):
    result = 0
    for c in s:
        result += ord(c)
        result *= 17
        result %= 256
    return result

part1 = 0
for step in data:
    part1 += HASH(step)
print("Part 1:", part1)

storage={}
for step in data:
    if step[-1]=='-':
        label = step[:-1]
        f=None
        try:
            del storage[label]
        except KeyError:
            continue            
    else:
        label = step[:step.index('=')]
        f=int(step[-1])
        storage[label]=f

part2 = 0
box_counts = [0 for x in range(256)]
for k in storage.keys(): # this relies on dicts being ordered by insertion; won't work before Python 3.6
    box_num = HASH(k)
    box_counts[box_num] += 1
    part2 += (1+box_num)*box_counts[box_num]*storage[k]
print("Part 2:", part2)
