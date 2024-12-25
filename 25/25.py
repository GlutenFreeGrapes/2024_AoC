import sys
# lines = [i.strip() for i in open(sys.argv[1]).readlines()]
line = open(sys.argv[1]).read()
blocks = line.split('\n\n')

keys = set()
locks = set()

key_heights = {}
lock_heights = {}

def height(block):
    h = [0,0,0,0,0]
    for line in block.split('\n'):
        for i in range(5):
            if line[i] == '#':
                h[i] += 1
    return tuple(h)

for block in blocks:
    if block.startswith('.....'):
        # is key
        keys.add(block)
        key_heights[block] = height(block)
    else:
        locks.add(block)
        lock_heights[block] = height(block)
print(key_heights)
print(lock_heights)

# part 1
count = 0
for key in key_heights:
    for lock in lock_heights:
        if all([(key_heights[key][i]+lock_heights[lock][i]) <= 7 for i in range(5)]):
            count += 1
print(count)
# part 2

"FINISHED"