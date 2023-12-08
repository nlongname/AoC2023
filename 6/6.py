import math

with open('input.txt', 'r+') as f:
    data = [line.strip('\n') for line in f.readlines()]

print("Day 6")
times = data[0][data[0].index(':')+1:].split()
t2 = int(''.join(times))
times = [int(t) for t in times]
distances = data[1][data[1].index(':')+1:].split()
d2 = int(''.join(distances))
distances = [int(d) for d in distances]

part1 = 1

for i in range(len(times)):
    t = times[i]
    d = distances[i]
    # say we hold the button for x ms
    # speed is x, time is t-x, so distance is x(t-x)
    # need x(t-x) >= d, so xt-x^2 >= d
    # x^2-xt+d <= 0
    # x = [t +/- sqrt(t^2 - 4d)]/2, take ceil of lower and floor of higher

    temp = (t-math.sqrt(t**2-4*d))/2
    lower = math.ceil(temp)
    if temp == lower:
        lower += 1
    temp = (t+math.sqrt(t**2-4*d))/2
    upper = math.floor(temp)
    if temp == upper:
        upper -= 1
    #print(lower, upper)

    count = upper-lower+1
    if count > 0:
        part1 *= count
print("Part 1:", part1)

t = t2
d = d2
temp = (t-math.sqrt(t**2-4*d))/2
lower = math.ceil(temp)
if temp == lower:
    lower += 1
temp = (t+math.sqrt(t**2-4*d))/2
upper = math.floor(temp)
if temp == upper:
    upper -= 1
print("Part 2:", upper-lower+1)
