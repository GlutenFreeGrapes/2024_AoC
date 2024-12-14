import sys, re


# lines = [i.strip() for i in open(sys.argv[1]).readlines()]
lines = re.findall(r'p\=(\-?\d+),(\-?\d+) v\=(\-?\d+),(\-?\d+)',open(sys.argv[1]).read())

X = int(sys.argv[2])
Y = int(sys.argv[3])

# MODULAR ARITHMETIC?
import numpy as np, re
# part 1
positions = {}
SECONDS = 100
for l in lines:
    pos = np.array([int(l[0]),int(l[1])])
    vel = np.array([int(l[2]),int(l[3])])
    end_pos = pos + (SECONDS * vel)
    ep_mod = (end_pos[0] % X, end_pos[1] % Y)
    if ep_mod in positions:
        positions[ep_mod] += 1
    else:
        positions[ep_mod] = 1

quads = {i:0 for i in range(4)}
# act as if middle index is 
mid_X = X // 2
mid_Y = Y // 2
for pos in positions:
    if pos[0] != mid_X and pos[1] != mid_Y:
        q = 0
        if mid_X > pos[0]:
            q += 1
        if mid_Y > pos[1]:
            q += 2 
        quads[q] += positions[pos]
safety = 1
for q in quads: safety *=quads[q]
print(safety)

# part 2
positions = {}
SECONDS = 0
while 1:
    map = [['.' for i in range(X)]for j in range(Y)]
    for l in lines:
        pos = np.array([int(l[0]),int(l[1])])
        vel = np.array([int(l[2]),int(l[3])])
        end_pos = pos + (SECONDS * vel)
        ep_mod = (end_pos[0] % X, end_pos[1] % Y)
        map[ep_mod[1]][ep_mod[0]] = '#'
    string_tree = '\n'.join([''.join(i) for i in map])
    open('tree.txt','w').write(string_tree)
    print(SECONDS)
    if string_tree.find('#'*6) + 1:
        input()
    SECONDS += 1
    