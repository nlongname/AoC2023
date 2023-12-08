from statistics import mode, StatisticsError

with open('input.txt', 'r+') as f:
    data = [line.strip('\n').split() for line in f.readlines()]
print("Day 7")

#concept: write hands as hex numbers with a preceding digit indicating how good the flush/streak/whatever is
# preceding digits is 0 for high card, 1 for pair, 2 for two-pair
# 3 for three-of-a-kind, 4 for full house, 5 for 4-of-a-kind, 6 for all five

translation = {'0':'0', '1':'1', '2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','T':'A','J':'B','Q':'C','K':'D', 'A':'E'}
def hexify(hand:str):
    new_hand = []
    for i in range(len(hand)):
        new_hand.append(translation[hand[i]])
    return ''.join(new_hand)


modification = {}
modified_hands = []

for l in data:
    hand = l[0]
    bid = l[1]
    count = len(set(hand))
    if count==5:
        modified_hands.append('0'+hand)
        modification[hand] = '0'+hand
    elif count == 4:
        modified_hands.append('1'+hand)
        modification[hand]='1'+hand
    elif count == 1:
        modified_hands.append('6'+hand)
        modification[hand]='6'+hand
    elif count == 2:
        max_count = 0
        for c in hand:
            max_count = max(max_count, hand.count(c))
        if max_count == 3:
            modified_hands.append('4'+hand)
            modification[hand]='4'+hand
        if max_count == 4:
            modified_hands.append('5'+hand)
            modification[hand]='5'+hand
    elif count == 3:
        max_count = 0
        for c in hand:
            max_count = max(max_count, hand.count(c))
        if max_count == 2:
            modified_hands.append('2'+hand)
            modification[hand]='2'+hand
        if max_count == 3:
            modified_hands.append('3'+hand)
            modification[hand]='3'+hand
modified_hands = sorted(modified_hands, key=lambda x: int(hexify(x), 16))

part1=0
for line in data:
    part1 += int(line[1])*(modified_hands.index(modification[line[0]])+1)

print("Part 1:", part1)


modification = {}
modified_hands = []
translation['J']='0'

for l in data:
    hand = l[0]
    bid = l[1]
    try:
        hand = hand.replace('J',mode([x for x in hand if x != 'J']))
    except StatisticsError:
        hand = 'JJJJJ'
    count = len(set(hand))
    if count==5:
        modified_hands.append('0'+l[0])
        modification[l[0]] = '0'+l[0]
    elif count == 4:
        modified_hands.append('1'+l[0])
        modification[l[0]]='1'+l[0]
    elif count == 1:
        modified_hands.append('6'+l[0])
        modification[l[0]]='6'+l[0]
    elif count == 2:
        max_count = 0
        for c in hand:
            max_count = max(max_count, hand.count(c))
        if max_count == 3:
            modified_hands.append('4'+l[0])
            modification[l[0]]='4'+l[0]
        if max_count == 4:
            modified_hands.append('5'+l[0])
            modification[l[0]]='5'+l[0]
    elif count == 3:
        max_count = 0
        for c in hand:
            max_count = max(max_count, hand.count(c))
        if max_count == 2:
            modified_hands.append('2'+l[0])
            modification[l[0]]='2'+l[0]
        if max_count == 3:
            modified_hands.append('3'+l[0])
            modification[l[0]]='3'+l[0]
modified_hands = sorted(modified_hands, key=lambda x: int(hexify(x), 16))

part2=0
for line in data:
    part2 += int(line[1])*(modified_hands.index(modification[line[0]])+1)

print("Part 2:", part2)
