import sys
input = open(sys.argv[1]).read()
is_free = False
current_id = 0
space = []
sp_no_nums = ''

# id to filesize as ordered list of tuples to make iteration easier
id_to_size = []

for i in input:
    if is_free:

        space += (['.'] * int(i))
        sp_no_nums += ('.' * int(i))

    else:
        id_to_size.append((len(space), int(i))) 

        space += ([str(current_id)] * (int(i)))
        sp_no_nums += ('X' * (int(i)))
        current_id += 1
    is_free = not is_free
print(len(space), current_id)

space_copy = space.copy()
sp_no_nums_copy = sp_no_nums
# part 1
import re
digits = re.compile('\d+')
# move over digits from end
for _ in range(space.count('.')):
    pd_index = space.index('.')
    # dig_index = digits.search(''.join(space)).span()[1] - 1
    dig_index = ''.join(sp_no_nums).rfind('X')
    if pd_index < dig_index:
        # swap
        space[pd_index] = space[dig_index]
        space[dig_index] = '.'

        # sp_no_nums[pd_index] = 'X'
        # sp_no_nums[dig_index] = '.'
        # space = space[:pd_index] + space[dig_index] + space[pd_index + 1:dig_index] + '.' + space[dig_index + 1:]
        sp_no_nums = sp_no_nums[:pd_index] + 'X' + sp_no_nums[pd_index + 1:dig_index] + '.' + sp_no_nums[dig_index + 1:]
        # print(space)
print(sum([int(i) * n for (n,i) in enumerate(space) if i != '.']))

# part 2
# use regex to count the spaces at each turn
# iterate through all id groups
for i in id_to_size[::-1]:
    # find the leftmost space gap that fits
    for j in re.finditer('\.+', sp_no_nums_copy[:i[0]]):
        # if gap is big enough
        if len(j.group(0)) >= i[1]:
            # swap
            pd_ind = j.span()[0]
            space_copy = space_copy[:pd_ind] + space_copy[i[0]: i[0]+i[1]] + space_copy[pd_ind + i[1]:i[0]] + space_copy[pd_ind: pd_ind + i[1]] + space_copy[i[0] + i[1]:]
            sp_no_nums_copy = sp_no_nums_copy[:pd_ind] + sp_no_nums_copy[i[0]: i[0]+i[1]] + sp_no_nums_copy[pd_ind + i[1]:i[0]] + sp_no_nums_copy[pd_ind: pd_ind + i[1]] + sp_no_nums_copy[i[0] + i[1]:]
            # print(''.join(space_copy))
            break
        # print(type(j))
        # print(j)

print(sum([int(i) * n for (n,i) in enumerate(space_copy) if i != '.']))

