from pprint import pprint

with open('input.txt', 'r+') as f:
    data = [line.strip('\n') for line in f.readlines()]
print("Day 16")

def next_loc(point, direction):
    y, x = point
    if direction == '>':
        return (y, x+1)
    elif direction == '<':
        return (y, x-1)
    elif direction == '^':
        return (y-1, x)
    elif direction == 'v':
        return (y+1, x)
    elif direction == None:
        return(y, x)

def behavior(tile, direction):
    if tile == '.':
        return [None]
    if tile == '|':
        if direction in ['<','>']:
            return ['^', 'v']
        else:
            return [direction]
    if tile == '-':
        if direction in ['^', 'v']:
            return ['<', '>']
        else:
            return [direction]
    if tile == '/':
        if direction == '>':
            return ['^']
        elif direction == '<':
            return ['v']
        elif direction == '^':
            return ['>']
        elif direction == 'v':
            return '<'
    if tile == '\\':
        if direction == '>':
            return ['v']
        elif direction == '<':
            return ['^']
        elif direction == '^':
            return ['<']
        elif direction == 'v':
            return '>'

def beam(location, direction):
    todo = [(location, direction)]
    history = set()
    energized = set()
    energized.add(location)
    while todo:
        location, direction = todo.pop()
        history.add((location, direction))
        y, x = next_loc(location, direction)
        if min(x, y) < 0 or x >= len(data[0]) or y >= len(data):
            continue
        energized.add((y, x))
        for new_dir in behavior(data[y][x], direction):
            if new_dir != None:
                if ((y, x), new_dir) not in history:
                    todo.append(((y, x), new_dir))
            else:
                if ((y, x), direction) not in history: 
                    todo.append(((y, x), direction))
    return len(energized)

print("Part 1:", beam((0,0), '>'))

#pprint([['#' if ((y, x) in energized) else '.' for x in range(len(data[0]))] for y in range(len(data))])

beams = [((0, x), 'v') for x in range(len(data[0]))]
beams += [((y,0), '>') for y in range(len(data))]
beams += [((y,len(data[0])-1), '<') for y in range(len(data))]
beams += [((len(data)-1, x), '^') for x in range(len(data[0]))]
print("Part 2:", max([beam(*b) for b in beams]))
