import sys
from collections import Counter
from math import log10

initial = open(sys.argv[1]).read()

def blink(line):
    newline = {}
    for i in line:
        if i == 0:
            if 1 in newline:
                newline[1] += line[i]
            else:
                newline[1] = line[i]
        elif int(log10(i)) % 2 == 1: # even digits
            s = str(i)
            splitting = len(s) // 2
            if int(s[:splitting]) in newline:
                newline[int(s[:splitting])] += line[i]
            else:
                newline[int(s[:splitting])] = line[i]
            if int(s[splitting:]) in newline:
                newline[int(s[splitting:])] += line[i]
            else:
                newline[int(s[splitting:])] = line[i]
        else:
            if i * 2024 in newline:
                newline[i * 2024] += line[i]
            else:
                newline[i * 2024] = line[i]
    return newline
# part 1
stones = dict(Counter([int(i) for i in initial.split()]))
for _ in range(25):
    print(_)
    stones = blink(stones)
print(sum(stones.values()))
# part 2
stones = dict(Counter([int(i) for i in initial.split()]))
for _ in range(75):
    print(_)
    stones = blink(stones)
print(sum(stones.values()))