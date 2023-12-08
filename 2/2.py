with open('input.txt', 'r+') as f:
    data = [line.strip('\n') for line in f.readlines()]

limits = {'red': 12, 'green': 13, 'blue': 14}

part1 = 0
part2 = 0

for line in data:
    line_id = int(line[5:line.index(':')])
    subgames = line[line.index(':')+2:].split(';')
    maxes = {'red': 0, 'green': 0, 'blue': 0}
    good_so_far = True
    for subgame in subgames:
        pulls = subgame.split(',')
        for pull in pulls:
            pull = pull.strip()
            color = pull[pull.index(' ')+1:]
            number = int(pull[:pull.index(' ')])
            maxes[color] = max(maxes[color], number)
            if number > limits[color]:
                good_so_far = False
    if good_so_far:
        part1 += line_id
    part2 += maxes['red']*maxes['green']*maxes['blue']

print("Day 2")
print("Part 1:", part1)
print("Part 2:", part2)
