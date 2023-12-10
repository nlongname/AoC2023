with open('input.txt', 'r+') as f:
    data = [[c for c in line.strip('\n')] for line in f.readlines()]
print("Day 10")

coords = None
for i in range(len(data)):
    if coords:
        break
    for j in range(len(data[0])):
        if data[i][j]=='S':
            current = 'S'
            coords = (i, j)
            break

i, j = coords
loop = [coords]
options = [None]
while options != []:
    current = data[i][j]
    options = []
    if i > 0 and data[i-1][j] in ['|', '7', 'F'] and current in ['S', '|', 'L', 'J']:
        options.append((i-1, j))
    if j > 0 and data[i][j-1] in ['-', 'L', 'F'] and current in ['S', '-', 'J', '7']:
        options.append((i, j-1))
    if i < (len(data)-1) and data[i+1][j] in ['|', 'L', 'J'] and current in ['S', '|','7', 'F']:
        options.append((i+1, j))
    if j < (len(data[0])-1) and data[i][j+1] in ['-', '7', 'J'] and current in ['S', '-', 'L', 'F']:
        options.append((i, j+1))
    options = [o for o in options if o not in loop]
    #print((i,j), options)
    if options:
        loop.append(options[0])
        i, j = options[0]
print("Part1:", len(loop)//2)

# Concept: if it's inside it has to cross the line an odd number of times to get to the edge
# if it's on the outside, it needs to cross an even number of times (incl. 0)
# to make this consistent, I'll be assuming we're going horizontal right above
# where the pipes are so it'll cross |, J, or L but not F, -, or 7


# bug-fixing step: need to figure out what shape S actually is
i, j = coords
neighbors = [loop[1], loop[-1]]
if (i-1, j) in neighbors:
    if (i+1, j) in neighbors:
        data[i][j] = '|'
    elif (i, j+1) in neighbors:
        data[i][j] = 'L'
    else:
        data[i][j] = 'J'
elif (i, j-1) in neighbors:
    if (i+1, j) in neighbors:
        data[i][j]='7'
    elif (i, j+1) in neighbors:
        data[i][j]='-'
else:
    data[i][j]='F'

internal = []
for i in range(len(data)):
    for j in range(len(data[0])):
        if (i, j) not in loop:
            data[i][j] = '.' # so that stray pipes aren't changing things
            # which means the only safe directions to look are left or up; left is simpler
            egress = data[i][:j]
            if (egress.count('|')+egress.count('J')+egress.count('L'))%2 == 1:
                internal.append((i, j))
print("Part 2:", len(internal))
