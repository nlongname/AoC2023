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
part2 = 0
for p in patterns:
    for c in range(1,len(p[0])): # c indicates columns to the left of the line
        d = min(c, len(p[0])-c)
        errors = sum([sum([line[c-d:c][i]!=line[c+d-1:c-1:-1][i] for i in range(d)]) for line in p])
        if errors == 0:
            part1 += c
        elif errors == 1:
            part2 += c
    for r in range(1,len(p)): # r indicates rows above the line
        d = min(r, len(p)-r)
        errors = sum([sum([p[i][j]!=p[2*r-i-1][j] for j in range(len(p[0]))]) for i in range(r-d,r)])
        if errors == 0:
            part1 += 100*r
        elif errors == 1:
            part2 += 100*r
print("Part 1:", part1)
print("Part 2:", part2)
