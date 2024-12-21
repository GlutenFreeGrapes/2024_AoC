import sys
lines = [i.strip() for i in open(sys.argv[1]).readlines()]
# line = open(sys.argv[1]).read()

num_keypad = [
    ['7','8','9'],
    ['4','5','6'],
    ['1','2','3'],
    [None,'0','A'],
]

dir_keypad = [
    [None, '^', 'A'],
    ['<', 'v', '>'],
]

# start at 'A'
num_locs = {num_keypad[i][j]:(i,j) for i in range(len(num_keypad)) for j in range(len(num_keypad[0]))}
arr_locs = {dir_keypad[i][j]:(i,j) for i in range(len(dir_keypad)) for j in range(len(dir_keypad[0]))}

# part 1
# generate ways to get from key to key 
def dist_to_arrows(dist_tuple):
    if dist_tuple[1] < 0:
        h = '<' * -dist_tuple[1]
    else:
        h = '>' * dist_tuple[1] 
    if dist_tuple[0] < 0:
        v = '^' * -dist_tuple[0]
    else:
        v = 'v' * dist_tuple[0] 
    return {h + v + 'A', v + h + 'A'}

num_key_dir = {}
for i in range(len(num_keypad)):
    for j in range(len(num_keypad[i])):
        element = num_keypad[i][j]
        for ii in range(len(num_keypad)):
            for jj in range(len(num_keypad[i])):
                element2 = num_keypad[ii][jj]
                if element and element2:
                    num_key_movements = dist_to_arrows((ii-i,jj-j))
                    num_key_dir[element,element2] = num_key_movements

arr_key_dir = {}
for i in range(len(dir_keypad)):
    for j in range(len(dir_keypad[i])):
        element = dir_keypad[i][j]
        for ii in range(len(dir_keypad)):
            for jj in range(len(dir_keypad[i])):
                element2 = dir_keypad[ii][jj]
                if element and element2:
                    arr_key_movements = dist_to_arrows((ii-i,jj-j))
                    arr_key_dir[element,element2] = arr_key_movements

DIRECTIONS = {
    '^':(-1,0),
    'v':(1,0),
    '<':(0,-1),
    '>':(0,1)
}
# check if solutions are viable
for i in num_key_dir:
    valid = {j:True for j in num_key_dir[i]}
    for instructions in num_key_dir[i]:
        loc = num_locs[i[0]]
        for keypress in instructions:
            if keypress in DIRECTIONS:
                d = DIRECTIONS[keypress]
                loc = (loc[0] + d[0], loc[1] + d[1])
                if loc == num_locs[None]:
                    valid[instructions] = False
                    break
    num_key_dir[i] = {j for j in num_key_dir[i] if valid[j]}

for i in arr_key_dir:
    valid = {j:True for j in arr_key_dir[i]}
    for instructions in arr_key_dir[i]:
        loc = arr_locs[i[0]]
        for keypress in instructions:
            if keypress in DIRECTIONS:
                d = DIRECTIONS[keypress]
                loc = (loc[0] + d[0], loc[1] + d[1])
                if loc == arr_locs[None]:
                    valid[instructions] = False
                    print(instructions)
                    break
    arr_key_dir[i] = {j for j in arr_key_dir[i] if valid[j]}

print(num_locs)
print(arr_locs)

for dir in (num_key_dir, arr_key_dir):
    for i in sorted(dir):
        print(i[0],i[1],dir[i])
    print()

# bfs to guarantee shortest path???
# from heapq import heappush, heappop
# def bfs(start, end, map):
#     f = [(0,start)]
#     visited = end
#     while len(start):
#         time, loc = heappop(f)
#         if bfs +=
#         for direction in DIRECTIONS:
            
# recursive function
import functools
@functools.cache
def instruction_recurse(instruction, depth):
    # maximum depth is the raw numberpad instructions
    # instruction is a single list of keypresses, return least length one
    # deepest case returns the user button presses
    # instruction is a single line of keypresses
    if depth == 1:
        # prev_loc = 'A'
        # m = ''
        # for keypress in instruction:
        #     if keypad_type[depth] == 'n':
        #         m+=tuple(num_key_dir[prev_loc, keypress])[0]
        #     else:
        #         m+=tuple(arr_key_dir[prev_loc, keypress])[0]
        #     prev_loc = keypress
        # return len(m),m
        return len(instruction)

    prev_loc = 'A'
    # possible_instructions = {''}
    res = 0
    possibilities = []
    # print(depth, instruction)
    for keypress in instruction:
        if instruction.isupper() and instruction.isalnum(): # if keypad_type[depth - 1] == 'n':
            # possibilities += [num_key_dir[prev_loc, keypress]]
            shortest_paths = num_key_dir[prev_loc, keypress]
        else:
            # possibilities += [arr_key_dir[prev_loc, keypress]]
            shortest_paths = arr_key_dir[prev_loc, keypress]
        # input(shortest_paths)
        res += min(instruction_recurse(sp, depth - 1) for sp in shortest_paths)
        prev_loc = keypress
    return res
    # for shortest_paths in possibilities:
    #     res += min(instruction_recurse(sp + 'A', depth - 1, keypad_type) for sp in shortest_paths)
    # return res



    # for keypress in instruction:
    #     # consider all possibilities
    #     new_poss = set()
    #     if keypad_type[depth] == 'n':
    #         for poss in possible_instructions:
    #             new_poss.update({poss + i for i in num_key_dir[prev_loc, keypress]})
    #         # possible_instructions = {p + i for i in num_key_dir[prev_loc, keypress] for p in possible_instructions}
    #     else:
    #         for poss in possible_instructions:
    #             new_poss.update({poss + i for i in arr_key_dir[prev_loc, keypress]})
    #         # possible_instructions = {p + i for i in arr_key_dir[prev_loc, keypress] for p in possible_instructions}
    #     possible_instructions = new_poss
    #     prev_loc = keypress
    # # base case: no fanangling with more bots, any solution will do
    # print(depth,possible_instructions)
    # instruction_instructions = {instruction_recurse(i, depth - 1, keypad_type)[1] for i in possible_instructions}
    # instruction_instructions = ((len(i),i) for i in instruction_instructions)
    # return min(instruction_instructions)        
            

        


keypad_order = ('k','k','k','n')

complexity = 0
for line in lines:
    numeric = int(line[:-1])
    m = instruction_recurse(line, len(keypad_order))
    # prev_movements = line
    # for instruction in ('n','k','k','k'):
    #     movements = []
    #     print(prev_movements)
    #     prev_loc = 'A'
    #     if instruction == 'n':
    #         for i in prev_movements:
    #             movements.append(num_key_dir[prev_loc, i])
    #             prev_loc = i
    #     else:
    #         for i in prev_movements:
    #             movements.append(arr_key_dir[prev_loc, i])
    #             prev_loc = i
    #     prev_movements = ''.join(movements)
    complexity += (numeric * m)
print(complexity)


# part 2
keypad_order = 'k'* 26 + 'n'

complexity = 0
for line in lines:
    numeric = int(line[:-1])
    m = instruction_recurse(line, len(keypad_order))
    complexity += (numeric * m)
print(complexity)