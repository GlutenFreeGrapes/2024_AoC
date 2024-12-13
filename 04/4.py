lines = [i.strip() for i in open('input.txt').readlines()]
# part 1
count = 0
find = 'XMAS'
for n, line in enumerate(lines):
    # horizontal
    count += line.count(find)
    count += line.count(find[::-1])

# vertical
for i in range(len(lines[0])):
    vert = ''.join([lines[n][i] for n in range(len(lines))])
    count += vert.count(find)
    count += vert.count(find[::-1])

# diags
import numpy as np
l = np.array([list(i) for i in lines])
l_rev = np.array([list(i)[::-1] for i in lines])

diag = ''.join(np.diagonal(l, offset = 0))
count+=diag.count(find)
count+=diag.count(find[::-1])
for i in range(1, len(lines)):
    diag = ''.join(np.diagonal(l, offset = -i))
    count+=diag.count(find)
    count+=diag.count(find[::-1])
for i in range(1, len(lines[0])):
    diag = ''.join(np.diagonal(l, offset = i))
    count+=diag.count(find)
    count+=diag.count(find[::-1])

diag = ''.join(np.diagonal(l_rev, offset = 0))
count+=diag.count(find)
count+=diag.count(find[::-1])
for i in range(1, len(lines)):
    diag = ''.join(np.diagonal(l_rev, offset = -i))
    count+=diag.count(find)
    count+=diag.count(find[::-1])
for i in range(1, len(lines[0])):
    diag = ''.join(np.diagonal(l_rev, offset = i))
    count+=diag.count(find)
    count+=diag.count(find[::-1])

# diagonal, ul to dr
# for n in range(len(lines)):
#     diag = ''.join([lines[n + i][i] for i in range(len(line))])

    # if n <= (len(lines) - len(find)):
    #     s = ''.join([lines[n + j][i] for j in range(len(find))])
    #     if s == find or s == find[::-1]:
    #         count+=1
    #     # diag, upper left to lower right
    #     if (i < (len(line) - len(find))):
    #         s_dul = ''.join([lines[n + j][i + j] for j in range(len(find))])
    #         print(1,s_dul)
    #         if s_dul == find or s_dul == find[::-1]:
    #             count+=1
    #     # diag, upper right to lower left
    #     if (i >= (len(find) - 1)):
    #         s_dur = ''.join([lines[n + j][i - j] for j in range(len(find))])
    #         print(2,s_dur)
    #         if s_dur == find or s_dur == find[::-1]:
    #             count+=1

        # rather than iterating, collect all lines instead
print(count)  

# part 2
# shift center around, get X-shape from there, check to see that spells "MAS" either way
find_set = {"MAS", "SAM"}
new_count = 0
for n in range(1, len(lines) - 1):
    for i in range(1, len(lines[n]) - 1):
        # where lines[n][i] is the center of the X
        main_diag = lines[n-1][i-1] + lines[n][i] + lines[n+1][i+1]
        opp_diag = lines[n+1][i-1] + lines[n][i] + lines[n-1][i+1]
        if main_diag in find_set and opp_diag in find_set:
            new_count +=1
print(new_count)