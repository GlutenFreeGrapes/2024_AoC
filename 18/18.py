import sys
lines = [i.strip() for i in open(sys.argv[1]).readlines()]
# line = open(sys.argv[1]).read()
coords = [tuple([int(j) for j in i.strip().split(',')]) for i in lines]
print(coords)

# part 1
SIZE = int(sys.argv[2]) + 1
map = [['.' for i in range(SIZE)] for j in range(SIZE)]


# place bits
NUM_COORDS = int(sys.argv[3])
for n in range(NUM_COORDS):
    map[coords[n][1]][coords[n][0]] = '#'

for i in map:
    print(''.join(i))

# bfs
MOVE_DIRECTIONS = {(0,-1),(0,1),(-1,0),(1,0)}
from heapq import heappop, heappush
def bfs_pathlen(start_loc):
    # heuristic: manhattan dist
    f = [((SIZE - start_loc[0] - 1) + (SIZE - start_loc[1] - 1), start_loc, (start_loc,))]
    visited = {start_loc}
    while len(f):
        dist, location, path = heappop(f)
        if location == (SIZE - 1, SIZE - 1):
            return path
        for d in MOVE_DIRECTIONS:
            new_loc = (location[0] + d[0], location[1] + d[1])
            if 0 <= new_loc[0] < SIZE and 0 <= new_loc[1] < SIZE and map[new_loc[1]][new_loc[0]] != '#' and new_loc not in visited:
                visited.add(new_loc)
                heappush(f, 
                         (len(path) + 1, new_loc, path + (new_loc,)))
                
print(len(bfs_pathlen((0,0)))-1)

# part 2
path = set(bfs_pathlen((0,0)))
for n in range(NUM_COORDS, len(coords)):
    map[coords[n][1]][coords[n][0]] = '#'
    if coords[n] in path:
        print(n)
        path = bfs_pathlen((0,0))
        if path:
            path = set(path)
        else:
            print(coords[n])
            break
        