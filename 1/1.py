with open('input.txt', 'r+') as f:
    data = [line.strip('\n') for line in f.readlines()]

print("Day 1")
result = 0
for line in data:
    digits = [c for c in line if c.isnumeric()]
    result += int(digits[0]+digits[-1])
print("Part 1: ", result)

digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']
numerify = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
for i in range(1,10):
    numerify[str(i)]=str(i)
result = 0
for line in data:
    start = min(digits, key=lambda x: line.find(x) if x in line else len(line))
    start = numerify[start]
    reversed_line = line[::-1]
    end = min(digits, key=lambda x: reversed_line.find(x[::-1]) if x[::-1] in reversed_line else len(line))
    end = numerify[end]
    result += int(start+end)
print("Part 2: ", result)
