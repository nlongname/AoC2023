with open('input.txt', 'r+') as f:
    data = [line.strip('\n') for line in f.readlines()]

print("Day 4")
part1 = 0

multiplicity = {}

g=1
for game in data:
    multiplicity[g] = 1 if g not in multiplicity else multiplicity[g]+1
    goal = game[game.find(':')+1:game.find('|')].split()
    ours = game[game.find('|')+1:].split()
    winning = [w for w in ours if w in goal]

    for i in range(len(winning)):
        multiplicity[g+i+1] = multiplicity[g] if g+i+1 not in multiplicity else multiplicity[g+i+1]+multiplicity[g]

    if winning != []:
        part1 += 2**(len(winning)-1)
    g += 1
print("Part 1:", part1)
part2 = sum(multiplicity.values())
print("Part 2:", part2)
