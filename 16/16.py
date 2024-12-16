import sys
lines = [i.strip() for i in open(sys.argv[1]).readlines()]
# line = open(sys.argv[1]).read()
start_loc = (-1,-1)
end_loc = (-1,-1)
bounds = set()

for n,i in enumerate(lines):
    for m,j in enumerate(i):
        if j == 'S':
            start_loc = (n,m)
        elif j == 'E':
            end_loc = (n,m)
        elif j == '#':
            bounds.add((n,m))

# part 1
from heapq import heappush, heappop
def bfs_score(turn_score, move_score):
    f = [(0,start_loc,(0,1))]
    visited = {start_loc:0}
    while len(f) > 0:
        score, location, dir = heappop(f)
        if end_loc in visited and score >= visited[end_loc]:return visited[end_loc]
        if location == end_loc:
            return score
        for direction in {(0,1),(0,-1),(1,0),(-1,0)}:
            new_location = (location[0] + direction[0], location[1] + direction[1])
            new_score = score + move_score
            if direction != dir:
                new_score += turn_score
            if new_location not in bounds and (new_location not in visited):# or new_score < visited[new_location]):
                heappush(f, (new_score, new_location, direction))
                visited[new_location] = new_score
    return None

print(bfs_score(1000, 1))

# part 2 - store path

def bfs_paths(turn_score, move_score):
    f = [(0,start_loc,(0,1), (start_loc,))]
    visited = {(start_loc, (0,1)):0}
    viable_paths = set()
    # intersections = set()

    progress = 0    

    while len(f) > 0:
        score, location, dir, path = heappop(f)

        if progress <= score: print(progress); progress += 1000

        if (end_loc,(-1,0)) in visited and score > visited[end_loc,(-1,0)]: return viable_paths
        if location == end_loc:
            print(score, end_loc, dir)
            if score == visited[end_loc,(-1,0)]:
                viable_paths.update(path)
        for direction in {i for i in {(0,1),(0,-1),(1,0),(-1,0)} if i!=(-1*dir[0],-1*dir[1])}:
            new_location = (location[0] + direction[0], location[1] + direction[1])
            new_score = score + move_score
            if direction != dir:
                new_score += turn_score
            if new_location not in bounds:
                if((new_location, direction) not in visited or new_score <= visited[(new_location, direction)]):
                    heappush(f, (new_score, new_location, direction, path + (new_location,)))
                    if new_location == end_loc:
                        print(direction)
                    if (new_location, direction) not in visited:
                        visited[(new_location, direction)] = new_score
                    else:
                        visited[(new_location, direction)] = visited[(new_location, direction)]
    return viable_paths
print(len(bfs_paths(1000, 1)))