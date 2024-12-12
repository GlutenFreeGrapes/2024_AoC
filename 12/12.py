import sys
initial = open(sys.argv[1]).readlines()

map = [list(i.strip()) for i in initial]

group_to_indices = {}

for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] in group_to_indices:
            group_to_indices[map[i][j]].add((i,j))
        else:
            group_to_indices[map[i][j]] = {(i,j)}

def flood_fill(map, index, group_to_fill):
    if not ((0 <= index[0] < len(map)) and (0 <= index[1] < len(map[0]))): return
    if map[index[0]][index[1]] == group_to_fill:
        map[index[0]][index[1]] = '.'
        flood_fill(map, (index[0] - 1, index[1]), group_to_fill)
        flood_fill(map, (index[0] + 1, index[1]), group_to_fill)
        flood_fill(map, (index[0], index[1] - 1), group_to_fill)
        flood_fill(map, (index[0], index[1] + 1), group_to_fill)

# something to handle non-continuous groups
group_to_indices_continuous = {}
for group in group_to_indices:
    current_id = 0
    for i in group_to_indices[group]:
        # check if index has been floodfilled
        already_placed = False
        for n in {j for j in group_to_indices_continuous.keys() if j.startswith(group)}:
            if i in group_to_indices_continuous[n]:
                already_placed = True
                break
        if not already_placed:
            # floodfill and pick all indices with . in them
            temp_map = [list(i.strip()) for i in initial]
            flood_fill(temp_map, i, group)
            # for line in temp_map:
            #     print(''.join(line))
            # print()

            group_to_indices_continuous[f'{group}_{current_id}'] = {(j, k) for j in range(len(temp_map)) for k in range(len(temp_map[j])) if temp_map[j][k] == '.'}
            # increment current_id
            current_id += 1
        
# part 1
cost = 0
for group in group_to_indices_continuous:
    group_area = len(group_to_indices_continuous[group])
    group_perimeter = 0
    for index in group_to_indices_continuous[group]:
        group_perimeter += len([i for i in {(index[0]+1,index[1]),(index[0]-1,index[1]),(index[0],index[1]+1),(index[0],index[1]-1)} if i not in group_to_indices_continuous[group]])
    print(group,group_area,group_perimeter)
    cost += (group_area * group_perimeter)
print(cost)

# part 2
cost = 0
for group in group_to_indices_continuous:
    group_area = len(group_to_indices_continuous[group])
    group_sides = 0
    group_corners = []
    for index in group_to_indices_continuous[group]:
        sides = [i for i in {(index[0]+1,index[1]),(index[0]-1,index[1]),(index[0],index[1]+1),(index[0],index[1]-1)} if i not in group_to_indices_continuous[group]]
        # there is at least 1 corner
        # if len(sides) == 2:
        #     print(index,sides)
        if len(sides) >= 2 and not (len(sides) == 2 and ((abs(sides[0][0]-sides[1][0]))==2 or abs(sides[0][1]-sides[1][1])==2)):
            if len(sides) < 4:
                print(index)

                group_sides += len(sides)-1
                group_corners.append(index)
            else:
                group_sides += 4

    group_indices_list = list(group_to_indices_continuous[group])
    # detect internal corners
    for n,i in enumerate(group_indices_list):
        for j in group_indices_list[n+1:]:
            if j!=i and abs(j[0]-i[0])==1 and abs(j[1]-i[1])==1:
                # diagonal 1 square from each other
                # if exactly one of the squares between them is in the group as well
                if len([k for k in {(i[0],j[1]), (j[0],i[1])} if k in group_to_indices_continuous[group]]) == 1:
                    group_sides += 1
    print(group,group_area,group_sides,group_corners)
    cost += (group_area * group_sides)
print(cost)