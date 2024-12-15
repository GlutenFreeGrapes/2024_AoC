import sys
lines = [i.strip() for i in open(sys.argv[1]).readlines()]
# line = open(sys.argv[1]).read()

# split map from directions
map = [i for i in lines if i.startswith('#')]
directions = ''.join([i for i in lines if i.strip() and not i.startswith('#')])

initial_loc = (-1,-1)
box_locs = set()
for n, i in enumerate(map):
    if '@' in i:
        initial_loc = (n, i.find('@'))
    for m, j in enumerate(i):
        if j == 'O':
            box_locs.add((n,m))
print('\n'.join(map))
print(initial_loc)

def draw_map(loc, boxes):
    s = ''
    for n, i in enumerate(map):
        for m, j in enumerate(i):
            if j == '#':
                s+='#'
            else:
                if (n,m) == loc:
                    s+='@'
                elif (n,m) in boxes:
                    s+='O'
                else:
                    s+='.'
        s+='\n'
    return s

import numpy as np
# all indices in (row, col) format
def next_empty_box(loc, offset):
    pos = loc
    while pos in box_locs:
        pos = (pos[0] + offset[0], pos[1] + offset[1])
        if map[pos[0]][pos[1]] == '#':
            return None
    return pos
# part 1
loc = initial_loc
for d in directions:
    if d == '<':
        offset = (0,-1)
    elif d == '>':
        offset = (0,1)
    elif d == '^':
        offset = (-1,0)
    else:
        offset = (1,0)
    new_loc = (loc[0] + offset[0], loc[1] + offset[1])
    if map[new_loc[0]][new_loc[1]]!='#':
        if new_loc in box_locs:
            s = next_empty_box(new_loc, offset)
            if s:
                box_locs.remove(new_loc)
                box_locs.add(s)
                loc = new_loc

        else:
            loc = new_loc

print(draw_map(loc, box_locs))
print(sum([100 * b[0] + b[1] for b in box_locs]))

            
        
# boxes now represented by a dict, key os [ location and value is ] location for convenience
new_boxes = {}
new_map = []
new_x = -1
for n,i in enumerate(map):
    new_map.append(i.replace('#','##').replace('O','[]').replace('.','..').replace('@','@.'))
    print(new_map[n])
    if '@' in new_map[n]:
        new_x = new_map[n].find('@')
    for m,j in enumerate(new_map[n]):
        if j == '[':
            new_boxes[(n,m)] = (n,m+1)
print(new_boxes)
def draw_map_new(loc, new_boxes):
    s = ''
    for n, i in enumerate(new_map):
        for m, j in enumerate(i):
            if j == '#':
                s+='#'
            else:
                if (n,m) == loc:
                    s+='@'
                elif (n,m) in new_boxes:
                    s+='['
                elif (n,m) in new_boxes.values():
                    s+=']'
                else:
                    s+='.'
        s+='\n'
    return s

def next_empty_box_vert(loc, offset):
    prev_affected = set()
    all_affected = set()
    if loc in new_boxes.values():
        affected_boxes = {loc, (loc[0], loc[1] - 1)}
    else:
        affected_boxes = {loc, (loc[0], loc[1] + 1)}
    while len(affected_boxes) > 0:
        prev_affected = affected_boxes
        all_affected.update(prev_affected)
        affected_boxes = set()
        # update boxes list with new boxes that would be affected by the push
        for i in prev_affected:
            new_box_loc = (i[0] + offset[0], i[1] + offset[1])
            if new_map[new_box_loc[0]][new_box_loc[1]] == '#':
                return None
            # get both sides of the new box and add them to the affected box set
            if new_box_loc in new_boxes.values():
                affected_boxes.update({new_box_loc, (new_box_loc[0], new_box_loc[1] - 1)})
            elif new_box_loc in new_boxes:
                affected_boxes.update({new_box_loc, (new_box_loc[0], new_box_loc[1] + 1)})
            
    return all_affected

def next_empty_box_horiz(loc, offset):
    affected_boxes = set()
    pos = loc
    while pos in new_boxes.keys() or pos in new_boxes.values():
        affected_boxes.add(pos)
        pos = (pos[0] + offset[0], pos[1] + offset[1])
        # if boxes hit wall, abort
        if new_map[pos[0]][pos[1]] == '#':
            return None
    return affected_boxes

# part 2
loc = (initial_loc[0], new_x)
print(loc)
print(draw_map_new(loc, new_boxes))
for d in directions:
    # print(loc,d)

    if d == '<':
        offset = (0,-1)
    elif d == '>':
        offset = (0,1)
    elif d == '^':
        offset = (-1,0)
    else:
        offset = (1,0)
    new_loc = (loc[0] + offset[0], loc[1] + offset[1])
    if new_map[new_loc[0]][new_loc[1]]!='#':
        if new_loc in new_boxes or new_loc in new_boxes.values():
            if d in '^v':
                affected = next_empty_box_vert(new_loc, offset)

            else:
                affected = next_empty_box_horiz(new_loc, offset)
            if affected:
                new_new_boxes = {}
                for n,j in enumerate(sorted(affected)):
                    if j in new_boxes:
                        o = new_boxes.pop(j)
                        new_new_boxes[(j[0]+offset[0], j[1]+offset[1])] = (o[0] + offset[0], o[1] + offset[1])
                new_boxes.update(new_new_boxes)
                loc = new_loc

        else:
            loc = new_loc
    # print(draw_map_new(loc, new_boxes))
    # input()

print(draw_map_new(loc, new_boxes))
print(sum([100 * b[0] + b[1] for b in new_boxes]))