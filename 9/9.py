with open('input.txt', 'r+') as f:
    data = [line.strip('\n').split() for line in f.readlines()]
print("Day 9")

part1 = 0
part2 = 0
for line in data:
    current = [int(x) for x in line]
    #print(current)
    front = [current[0]]
    back = [current[-1]]
    while any(current) == True:
        current = [current[i+1]-current[i] for i in range(len(current)-1)]
        back.append(current[-1])
        front.append(current[0])
        #print(current)
    #print(sum(trail))
    part1 += sum(back)
    #print(front)
    part2 += sum([front[i]*(-1)**(i) for i in range(len(front))]) # getting alternately subtracted each round, rather than added
print("Part 1:", part1)
print("Part 2:", part2)
