from functools import cache

with open('input.txt', 'r+') as f:
    data = [line.strip('\n') for line in f.readlines()]
print("Day 14")

rollers = []
stoppers = set()

for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == 'O':
            rollers.append((y,x))
        elif data[y][x] == '#':
            stoppers.add((y,x))

original_rollers = [r for r in rollers]

done_rolling = set()
while rollers:
    new_rollers = [] # so we aren't mutating
    for r in rollers:
        y,x = r
        if y == 0 or (y-1, x) in stoppers or (y-1, x) in done_rolling:
            done_rolling.add(r)
        else:
            new_rollers.append((y-1, x))
    rollers = new_rollers
part1 = sum(len(data)-r[0] for r in done_rolling)
print("Part 1:", part1)

def cycle(rollers):
    rollers = sorted(list(rollers), key=lambda r: r[0])
    done_rolling = set()
    # north
    while rollers:
        new_rollers = [] # so we aren't mutating
        for r in rollers:
            y,x = r
            if y == 0 or (y-1, x) in stoppers or (y-1, x) in done_rolling:
                done_rolling.add(r)
            else:
                new_rollers.append((y-1, x))
        rollers = new_rollers

    # west
    rollers = sorted(list(done_rolling), key=lambda r: r[1])
    done_rolling = set()
    while rollers:
        new_rollers = [] # so we aren't mutating
        for r in rollers:
            y,x = r
            if x==0 or (y, x-1) in stoppers or (y, x-1) in done_rolling:
                done_rolling.add(r)
            else:
                new_rollers.append((y, x-1))
        rollers = new_rollers

    # south
    rollers = sorted(list(done_rolling), key=lambda r: r[0], reverse=True)
    done_rolling = set()
    while rollers:
        new_rollers = [] # so we aren't mutating
        for r in rollers:
            y,x = r
            if y == len(data)-1 or (y+1, x) in stoppers or (y+1, x) in done_rolling:
                done_rolling.add(r)
            else:
                new_rollers.append((y+1, x))
        rollers = new_rollers

    # east
    rollers = sorted(list(done_rolling), key=lambda r: r[1], reverse=True)
    done_rolling = set()
    while rollers:
        new_rollers = [] # so we aren't mutating
        for r in rollers:
            y,x = r
            if x==len(data[0])-1 or (y, x+1) in stoppers or (y, x+1) in done_rolling:
                done_rolling.add(r)
            else:
                new_rollers.append((y, x+1))
        rollers = new_rollers
    return tuple(sorted(list(done_rolling)))

rollers = tuple(sorted([r for r in original_rollers]))
roll_cache = {rollers:-1}
num_cycles = 1000000000
for i in range(num_cycles):
    rollers = cycle(rollers)
    if rollers in roll_cache:
        cycle_length = i - roll_cache[rollers]
        #print(i, cycle_length)
        target = (num_cycles-i-1)%cycle_length + (i-cycle_length)
        rollers = [x for x in roll_cache if roll_cache[x]==target][0]
        break
    roll_cache[rollers] = i
print("Part 2:", sum(len(data)-r[0] for r in rollers))
