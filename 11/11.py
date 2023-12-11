with open('input.txt', 'r+') as f:
    data = [[c for c in line.strip('\n')] for line in f.readlines()]
print("Day 11")

from pprint import pprint

x_expansion = []
y_expansion = []

for x in range(len(data[0])):
    if all([data[y][x]=='.' for y in range(len(data))]):
        x_expansion.append(x)

for y in range(len(data)):
    if data[y].count('#') == 0:
        y_expansion.append(y)

galaxies = []
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == '#':
            galaxies.append((y, x))

def total_distances(galaxies, expansion_constant=1):
    total = 0
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            low_x, high_x = min(galaxies[i][1], galaxies[j][1]), max(galaxies[i][1], galaxies[j][1])
            low_y, high_y = min(galaxies[i][0], galaxies[j][0]), max(galaxies[i][0], galaxies[j][0])

            total += ((high_x-low_x) + (high_y-low_y))

            total += (expansion_constant-1)*len([y for y in y_expansion if low_y < y and y < high_y])
            total += (expansion_constant-1)*len([x for x in x_expansion if low_x < x and x < high_x])
    return total

print("Part 1:", total_distances(galaxies, 2))
print("Part 2:", total_distances(galaxies, 1000000))
