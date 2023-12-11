with open('test_input.txt', 'r+') as f:
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
x_expansion = []
while x < len(new_data[0]):
    if all([new_data[y][x]=='.' for y in range(len(new_data))]):
        x_expansion.append(x)
    x += 1

newer_data = []
for y in range(len(new_data)):
    newer_data.append([])
    for x in range(len(new_data[0])):
        newer_data[y].append(new_data[y][x])
        if x in x_expansion:
            newer_data[y].append('.')
pprint(newer_data)
