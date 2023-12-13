from pprint import pprint

with open('input.txt', 'r+') as f:
    data = [line.strip('\n') for line in f.readlines()]
print("Day 13")

patterns = []

i = 0
while i < len(data):
    try:
        pattern = data[i:data.index('', i)]
    except ValueError:
        pattern = data[i:]
    i += len(pattern)+1
    patterns.append(pattern)

part1 = 0
for p in patterns:
    found = [False, False]
    for c in range(1,len(p[0])): # c indicates columns to the left of the line
        d = min(c, len(p[0])-c)
        if all([line[c-d:c]==line[c+d-1:c-1:-1] for line in p]):
            part1 += c
            found[0] = True
    for r in range(1,len(p)): # r indicates rows above the line
        d = min(r, len(p)-r)
        if all([p[i]==p[2*r-i-1] for i in range(r-d, r+d)]):
            part1 += 100*r
            found[1] = True
    if not found[0] and not found[1]:
        pprint(p)
print("Part 1:", part1)
