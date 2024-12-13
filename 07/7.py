def eval(nums, ops):
    s = nums[0]
    for i in range(1, len(nums)):
        if ops[i-1] == '+':
            s+=nums[i]
        elif ops[i-1] == '*':
            s*=nums[i]
        else:
            s = int(str(s)+str(nums[i]))
    return s
from itertools import product

# part 1
possible_sum = 0
for line in open('input.txt').readlines():
    sections = line.split(':')
    goal = int(sections[0])
    numbers = tuple(int(i) for i in sections[1].strip().split())
    for i in product('+*',repeat=(len(numbers) - 1)):
        if eval(numbers, i) == goal:
            possible_sum += goal
            break
print(possible_sum)

# part 2
possible_sum = 0
for line in open('input.txt').readlines():
    sections = line.split(':')
    goal = int(sections[0])
    numbers = tuple(int(i) for i in sections[1].strip().split())
    for i in product('+*|',repeat=(len(numbers) - 1)):
        if eval(numbers, i) == goal:
            possible_sum += goal
            break
print(possible_sum)