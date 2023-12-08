with open('input.txt', 'r+') as f:
    data = [line.strip('\n') for line in f.readlines()]

print("Day 3")
part1 = 0

gears = {}

for j in range(len(data)):
    line = data[j]
    i=0
    while i < len(line):
        while i < len(line) and not line[i].isnumeric():
            i += 1
        if i == len(line):
            continue
        start = i
        while i < len(line) and line[i].isnumeric():
            i += 1
        end = i-1
        symbol = False
        for x in range(max(0, start-1), min(len(line), end+2)):
            for y in range(max(0, j-1), min(len(data), j+2)):
                if data[y][x] != '.' and not data[y][x].isnumeric():
                    symbol = True
                    if data[y][x] == '*':
                        index = y*len(line)+x
                        if index not in gears:
                            gears[index] = []
                        gears[index] +=  [int(line[start:end+1])]
                    break
            if symbol:
                break
        if symbol:
            part1 += int(line[start:end+1])
            #print(int(line[start:end+1]))
part2 = sum([v[0]*v[1] for k,v in gears.items() if len(v)==2])
print("Part 1:", part1)
print("Part 2:", part2)
