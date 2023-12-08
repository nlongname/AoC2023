with open('input.txt', 'r+') as f:
    data = [line.strip('\n') for line in f.readlines()]

print("Day 5")
seeds = data[0][data[0].index(':')+1:].split()
seeds = [int(s) for s in seeds]


s2s = data[data.index('seed-to-soil map:')+1:data.index('soil-to-fertilizer map:')-1]
s2s = [[int(x) for x in link.split()] for link in s2s]

s2f = data[data.index('soil-to-fertilizer map:')+1:data.index('fertilizer-to-water map:')-1]
s2f = [[int(x) for x in link.split()] for link in s2f]

f2w = data[data.index('fertilizer-to-water map:')+1:data.index('water-to-light map:')-1]
f2w = [[int(x) for x in link.split()] for link in f2w]

w2l = data[data.index('water-to-light map:')+1:data.index('light-to-temperature map:')-1]
w2l = [[int(x) for x in link.split()] for link in w2l]

l2t = data[data.index('light-to-temperature map:')+1:data.index('temperature-to-humidity map:')-1]
l2t = [[int(x) for x in link.split()] for link in l2t]

t2h = data[data.index('temperature-to-humidity map:')+1:data.index('humidity-to-location map:')-1]
t2h = [[int(x) for x in link.split()] for link in t2h]

h2l = data[data.index('humidity-to-location map:')+1:]
h2l = [[int(x) for x in link.split()] for link in h2l]

locations = []
for seed in seeds:
    current = seed
    for chain in [s2s, s2f, f2w, w2l, l2t, t2h, h2l]:
        for link in chain:
            if current >= link[1] and current-link[1] < link[2]:
                current += link[0]-link[1]
                #print(current)
                break    
    locations.append(current)
print("Part 1:", min(locations))

# way too many to go forwards in part 2, let's try going backwards?

location = 0
part2=None
while not part2:
    current = location
    for chain in [h2l, t2h, l2t, w2l, f2w, s2f, s2s]:
        for link in chain:
            if current >= link[0] and current-link[0] < link[2]:
                current += link[1]-link[0]
                #print(current)
                break
    for s in range(0,len(seeds),2):
        if seeds[s] <= current and seeds[s]+seeds[s+1]>current:
            part2=location
            break
    location += 1

print("Part 2:", part2)
# this works, but it's super slow
