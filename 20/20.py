import sys
lines = [i.strip() for i in open(sys.argv[1]).readlines()]
# line = open(sys.argv[1]).read()

start_loc = (-1,-1)
end_loc = (-1,-1)
bounds = set()
MOVE_DIRECTIONS = {(0,-1),(0,1),(-1,0),(1,0)}

for n, i in enumerate(lines):
    for m, j in enumerate(i):
        if j == 'E':
            end_loc = (n,m)
        elif j == 'S':
            start_loc = (n,m)
        elif j == '#':
            bounds.add((n,m))

ROWS = len(lines)
COLS = len(lines[0])

# part 1
from heapq import heappop, heappush
from collections import Counter
def bfs(bounds):
    f = [(0,start_loc, (start_loc,))]
    visited = {start_loc}
    while len(f):
        time, location, path = heappop(f)
        if location == end_loc:
            return time, path
        for d in MOVE_DIRECTIONS:
            new_loc = (location[0] + d[0], location[1] + d[1])
            if 0 <= new_loc[0] < ROWS and 0 <= new_loc[1] < COLS and new_loc not in visited and new_loc not in bounds:
                heappush(f,(time+1,new_loc, path+(new_loc,)))
                visited.add(new_loc)
default_end, default_path = bfs(bounds)

coord_to_dist = {i:n for n,i in enumerate(default_path)}

default_path_walls = bounds.intersection({(i[0] + d[0], i[1] + d[1]) for d in MOVE_DIRECTIONS for i in default_path}.difference(default_path))

print(default_end)

# brute force
sols = []
visited_cheats = set()
# for i in range(len(lines)):
#     print(i)
#     for j in range(len(lines[i])):
#         print(i,j)
for (i,j) in bounds:
    if ((0 < i < (ROWS - 1)) and (i - 1, j) not in bounds and (i + 1, j) not in bounds):
        sols.append(min(default_end, coord_to_dist[(i - 1, j)] + 1 + (default_end - coord_to_dist[(i + 1, j)]), coord_to_dist[(i + 1, j)] + 1 + (default_end - coord_to_dist[(i - 1, j)])))
    elif ((0 < j < (COLS - 1)) and (i, j - 1) not in bounds and (i, j + 1) not in bounds):
        sols.append(min(default_end, coord_to_dist[(i, j - 1)] + 1 + (default_end - coord_to_dist[(i, j + 1)]), coord_to_dist[(i, j + 1)] + 1 + (default_end - coord_to_dist[(i, j - 1)])))
        
        # print(i,j)
        
        # if (i,j) in default_path_walls:
        # sols.append(bfs(bounds - {(i,j)})[0])
        # visited_cheats.add((i,j))

        # # pick horizontally adjacent pairs to set to ..
        # to_remove = {(i, j),(i, j + 1)}
        # if j+1 < COLS:
        #     new_bounds = bounds.difference(to_remove)

        #     if len(new_bounds) != len(bounds) and tuple(sorted(new_bounds)) not in visited_cheats and len(default_path_walls.intersection(to_remove)):
        #         sols.append(bfs(new_bounds)[0])
        #         if sols[-1] == 20:
        #             print(to_remove)
        #         visited_cheats.add(tuple(sorted(new_bounds)))

        # # pick vertically adjacent pairs to set to ..
        # to_remove = {(i, j),(i + 1, j)}
        # if i+1 < ROWS:
        #     new_bounds = bounds.difference(to_remove)
        #     if len(new_bounds) != len(bounds) and tuple(sorted(new_bounds)) not in visited_cheats and len(default_path_walls.intersection(to_remove)):
        #         sols.append(bfs(new_bounds)[0])
        #         if sols[-1] == 20:
        #             print(to_remove)
        #         visited_cheats.add(tuple(sorted(new_bounds)))

solutions = dict(Counter(sols))
print(sorted(zip(solutions.keys(),solutions.values())))
print(sum([solutions[i] for i in solutions if (default_end - i) >= 100]))



# part 2
sols = {}
# use manhattan distance to determine cheat length
# find all non-wall coord pairs within 20 of coordinate pairs
cheat_offsets = {(i,j) for i in range(-20,21) for j in range(-20,21) if 1 < (abs(i)+abs(j)) <= 20}


for coord in sorted(coord_to_dist):
    
    # min_dist = default_end + 1
    # for d in MOVE_DIRECTIONS:
    #     new_loc = (coord[0] + d[0], coord[1] + d[1])
    #     if 0 <= new_loc[0] < ROWS and 0 <= new_loc[1] < COLS and new_loc in coord_to_dist:
    #         min_dist = min(min_dist, coord_to_dist[new_loc] + 1)
    # if min_dist != (default_end + 1):
        for offset in cheat_offsets:
                    cheat_dist = abs(offset[0]) + abs(offset[1])
                    new_coord = (coord[0] + offset[0], coord[1] + offset[1])

                    # make sure this is actually a cheat

                    if (min(coord, new_coord), max(coord, new_coord)) not in sols:
                        if new_coord in coord_to_dist:
                            sols[(min(coord, new_coord), max(coord, new_coord))] = (coord_to_dist[coord] + (cheat_dist) + (default_end - coord_to_dist[new_coord]))
                        
                            # print(coord, new_coord, default_end, coord_to_dist[coord] + (cheat_dist) + (default_end - coord_to_dist[new_coord]))
                    else:
                        if new_coord in coord_to_dist:
                            sols[(min(coord, new_coord), max(coord, new_coord))] = (min(sols[(min(coord, new_coord), max(coord, new_coord))], coord_to_dist[coord] + (cheat_dist) + (default_end - coord_to_dist[new_coord])))

solutions = dict(Counter(sols.values()))
print(sorted(zip(solutions.keys(),solutions.values())))
print(sum([solutions[i] for i in solutions if (default_end - i) >= 100]))