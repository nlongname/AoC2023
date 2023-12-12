from functools import lru_cache

with open('input.txt', 'r+') as f:
    data = [line.strip('\n') for line in f.readlines()]
print("Day 12")

# concept: if we sum up all the damaged springs plus the undamaged delimiters
# see how many springs we have left, and that sets a limit on how far "off"
# they can be from just being packed to the left
# e.g. 2 extra springs, so first damaged can be 0, 1, or 2 unless specified
# then take out that part and recurse on the remaining substring

@lru_cache
def combos(string:str, chunks:tuple) -> int:
    if chunks == () or string == '':
        if string.count('#') == 0:
            return 1
        else:
            return 0
    string = string.strip('.')
    min_length = sum(chunks)+len(chunks)-1
    if min_length > len(string):
        return 0
    elif min_length == len(string):
        test_string = ''
        for c in chunks:
            test_string += (('#')*c+'.')
        test_string = test_string[:-1]
        if all([string[i] == test_string[i] or string[i] == '?' for i in range(len(string))]):
            return 1
        else:
            return 0
    else:
        max_offset = len(string)-min_length
        total = 0
        first = 0 # I stripped the periods, so this will always be '?' or '#'
        while first <= max_offset:
            if string[:first].count('#') != 0:
                break
            if string[first:first+chunks[0]].count('.') == 0 and (len(string)==first+chunks[0] or string[first+chunks[0]] != '#'):
                subtotal = combos(string[first+chunks[0]+1:].strip('.'), chunks[1:])
                total += subtotal
            first += 1
            if first > len(string):
                break
        return total

part1 = 0
part2 = 0
for line in data:
    s = line[:line.index(' ')]
    s2 = (s+'?')*4+s
    c = tuple(int(c) for c in line[line.index(' '):].split(','))
    c2 = c*5
    part1 += combos(s, c)
    part2 += combos(s2, c2)
    #print(s, c, combos(s,c))
    #print(data.index(line), s2, c2, combos(s2, c2))
print("Part 1:", part1)
print("Part 2:", part2)
