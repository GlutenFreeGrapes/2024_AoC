import sys
lines = open(sys.argv[1]).read()
map = []
initial_loc = [-1,-1]
for n,i in enumerate(lines.split('\n')):
    map.append(list(i))
    if '^' in i:
        initial_loc = [n, i.find('^')]
print(map)
print(initial_loc)

initial_map = '\n'.join([''.join(i) for i in map])
loc = list(initial_loc)

def out_of_bounds(loc, direction):
    return ((1 and loc[0] == -1) or (1 and loc[0] == len(map))
        or (1 and loc[1] == -1) or (1 and loc[1] == len(map[0])))

def pretty_print():
    for i in map:
        print(''.join(i))

DIRECTIONS = 'nesw'
# part 1
direction = 'n'
while (not out_of_bounds(loc, direction)):
    # nothing in direction facing
    # print(loc, direction)
    # pretty_print()
    map[loc[0]][loc[1]] = 'X'
    match direction:
        case 'n':
            loc[0] -= 1
            if out_of_bounds(loc, direction): loc[0] +=1; map[loc[0]][loc[1]] = 'X'; break
            if map[loc[0]][loc[1]] == '#':
                direction = DIRECTIONS[(DIRECTIONS.index(direction) + 1) % 4]
                loc[0] += 1
            map[loc[0]][loc[1]] = '^'
        case 's':
            loc[0] += 1
            if out_of_bounds(loc, direction): loc[0] -=1; map[loc[0]][loc[1]] = 'X'; break
            if map[loc[0]][loc[1]] == '#':
                direction = DIRECTIONS[(DIRECTIONS.index(direction) + 1) % 4]
                loc[0] -= 1
            map[loc[0]][loc[1]] = 'v'
        case 'w':
            loc[1] -= 1
            if out_of_bounds(loc, direction): loc[1] +=1; map[loc[0]][loc[1]] = 'X'; break
            if map[loc[0]][loc[1]] == '#':
                direction = DIRECTIONS[(DIRECTIONS.index(direction) + 1) % 4]
                loc[1] += 1
            map[loc[0]][loc[1]] = '<'
        case 'e':
            loc[1] += 1
            if out_of_bounds(loc, direction): loc[1] -=1; map[loc[0]][loc[1]] = 'X'; break
            if map[loc[0]][loc[1]] == '#':
                direction = DIRECTIONS[(DIRECTIONS.index(direction) + 1) % 4]
                loc[1] -= 1
            map[loc[0]][loc[1]] = '>'
    # print(loc)
    # print()
        # case 's':
            # if out_of_bounds(loc, direction) or map[loc[0] + 1][loc[1]] == '#':
print(''.join([''.join(i) for i in map]).count("X"))
# part 2
positions = 0
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == '.':
            map[i][j] = '#'

            loc = list(initial_loc)

            visited = set()
            passed = False
            while (not out_of_bounds(loc, direction)):
                # nothing in direction facing
                # print(loc, direction)
                # pretty_print()
                map[loc[0]][loc[1]] = 'X'
                c = tuple(loc) + (direction,)
                if c in visited: 
                    passed = True; 
                    break 
                else: 
                    visited.add(c)

                match direction:
                    case 'n':
                        loc[0] -= 1
                        if out_of_bounds(loc, direction): loc[0] +=1; map[loc[0]][loc[1]] = 'X'; break
                        if map[loc[0]][loc[1]] == '#':
                            direction = DIRECTIONS[(DIRECTIONS.index(direction) + 1) % 4]
                            loc[0] += 1
                        map[loc[0]][loc[1]] = '^'
                    case 's':
                        loc[0] += 1
                        if out_of_bounds(loc, direction): loc[0] -=1; map[loc[0]][loc[1]] = 'X'; break
                        if map[loc[0]][loc[1]] == '#':
                            direction = DIRECTIONS[(DIRECTIONS.index(direction) + 1) % 4]
                            loc[0] -= 1
                        map[loc[0]][loc[1]] = 'v'
                    case 'w':
                        loc[1] -= 1
                        if out_of_bounds(loc, direction): loc[1] +=1; map[loc[0]][loc[1]] = 'X'; break
                        if map[loc[0]][loc[1]] == '#':
                            direction = DIRECTIONS[(DIRECTIONS.index(direction) + 1) % 4]
                            loc[1] += 1
                        map[loc[0]][loc[1]] = '<'
                    case 'e':
                        loc[1] += 1
                        if out_of_bounds(loc, direction): loc[1] -=1; map[loc[0]][loc[1]] = 'X'; break
                        if map[loc[0]][loc[1]] == '#':
                            direction = DIRECTIONS[(DIRECTIONS.index(direction) + 1) % 4]
                            loc[1] -= 1
                        map[loc[0]][loc[1]] = '>'
            
            
            # pretty_print()
            # print()
            map = [list(k) for k in initial_map.split('\n')]
            direction = 'n'
            if passed:
                positions += 1
                print(i,j, positions)

print(positions)