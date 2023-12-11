with open('input.txt', 'r+') as f:
    data = [[c for c in line.strip('\n')] for line in f.readlines()]
print("Day 11")

from pprint import pprint

new_data = []

y=0
while y < len(data):
    if data[y].count('#') == 0:
        new_data.append(data[y])
    new_data.append(data[y])
    y += 1
#pprint(new_data)
#print(len(new_data))

x = 0
while x < len(new_data[0]):
    if all([new_data[y][x]=='.' for y in range(len(new_data))]):
        new_data = [new_data[y][:x]+['.']+new_data[y][x:] for y in range(len(new_data))]
        x += 1
    x += 1

data = new_data

galaxies = []
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == '#':
            galaxies.append((y, x))

total = 0
for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        total += abs(galaxies[i][0]-galaxies[j][0]) + abs(galaxies[i][1]-galaxies[j][1])

print("Part 1:", total)
