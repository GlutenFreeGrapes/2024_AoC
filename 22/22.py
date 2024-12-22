import sys
lines = [int(i.strip()) for i in open(sys.argv[1]).readlines()]
# line = open(sys.argv[1]).read()

# part 1
import functools
@functools.cache
def nextnum(input_num):
    input_num = (input_num ^ (input_num << 6)) & ((1<<24)-1)
    input_num = (input_num ^ (input_num >> 5)) & ((1<<24)-1)
    input_num = (input_num ^ (input_num << 11)) & ((1<<24)-1)
    return input_num

secret_num_ones = []
secret_num_ones_diffs = []

s = 0

# maps difference in ones digit to a character
digits = 'ABCDEFGHIJabcdefghi'
for i in lines:
    ones = (i%10,)
    diffs = 'A'
    prev_ones = i%10
    for _ in range(2000):
        i = nextnum(i)
        ones += (i%10,)
        diffs += digits[(i%10) - prev_ones]
        prev_ones = i%10
    s+=i
    secret_num_ones.append(ones)
    secret_num_ones_diffs.append(diffs)
print(s)

# part 2

def eval_seq(seq):
    # iterate through all buyers
    sold = 0
    for i in range(len(secret_num_ones)):
    # check for sequence membership in the ones
        if seq in secret_num_ones_diffs[i]:
            banana_index = secret_num_ones_diffs[i].find(seq) + 3

            # if so, add the number at the end to sold
            sold += secret_num_ones[i][banana_index]
    return sold


from collections import Counter
all_substrings = []
for i in secret_num_ones_diffs:
    substrings = {i[j:j+4] for j in range(len(i) - 3)}
    all_substrings.extend(substrings)
substring_count = Counter(all_substrings)
print(len(substring_count))
max_sold = 0
for n,i in sorted(zip(substring_count.values(),substring_count.keys()),reverse=1):
    if n>1:
        print(i,substring_count[i])
        max_sold = max(max_sold,eval_seq(i))
print(max_sold)