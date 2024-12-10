import sys
map = [[int(j) if j.isnumeric() else -1 for j in i.strip()] for i in open(sys.argv[1]).readlines()]

# impossible = {}

def bfs_score(start_location):
    poss = 0
    visited = {start_location}
    f = [start_location]
    while len(f) > 0:
        current_loc = f.pop()
        if map[current_loc[0]][current_loc[1]] == 9:
            poss += 1
        else:
            children = [(i,j) for (i,j) in [(current_loc[0] + 1, current_loc[1]), (current_loc[0] - 1, current_loc[1]),(current_loc[0], current_loc[1]+1),(current_loc[0], current_loc[1]-1)] if (0 <= i < len(map)) and (0 <= j < len(map[0])) and (map[current_loc[0]][current_loc[1]] + 1 == map[i][j])]
            for next in children:
                if next not in visited:
                    f.append(next)
                    visited.add(next)
    return poss

# part 1
scores = 0
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == 0:
            scores += bfs_score((i,j))
print(scores)

def bfs_rating(start_location):
    poss = 0
    visited = {start_location}
    f = [start_location]
    while len(f) > 0:
        current_loc = f.pop()
        if map[current_loc[0]][current_loc[1]] == 9:
            poss += 1
        else:
            children = [(i,j) for (i,j) in [(current_loc[0] + 1, current_loc[1]), (current_loc[0] - 1, current_loc[1]),(current_loc[0], current_loc[1]+1),(current_loc[0], current_loc[1]-1)] if (0 <= i < len(map)) and (0 <= j < len(map[0])) and (map[current_loc[0]][current_loc[1]] + 1 == map[i][j])]
            for next in children:
                # if next not in visited:
                    f.append(next)
                    visited.add(next)
    return poss

# part 2
ratings = 0
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == 0:
            ratings += bfs_rating((i,j))
print(ratings)