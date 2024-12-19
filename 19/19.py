import sys
lines = [i.strip() for i in open(sys.argv[1]).readlines()]
# line = open(sys.argv[1]).read()

towels = set(lines[0].split(', '))
# part 1
def bfs(word):
    f = ['']
    visited = set()
    while len(f):
        w = f.pop()
        if w == word:
            return True        
        for t in towels:
            new_word = w + t
            if word.startswith(new_word):
                f.append(new_word)
                visited.add(new_word)
    return False
solvable = [bfs(i) for i in lines[2:]]
print(sum(solvable))


# part 2
print(towels)
import functools
@functools.cache
def words_solvable(word, is_right):
    # base case
    if len(word) == 1:
        return word in towels
    
    if is_right:
        ways = 0
        for i in range(1, len(word)):
            lh = words_solvable(word[:i], False)
            rh = words_solvable(word[i:], True)
            ways += lh * rh
        return (word in towels) + ways
    return word in towels

# print(words_solvable('rr'))
print(words_solvable(lines[2], True))


# def bfs_ways(word):
#     # first part of substring to # of ways to solve?
    
#     # solve recursively?

#     f = {('',tuple())}
#     visited = set()
#     ways = set()
#     while len(f):
#         w, way = f.pop()
#         if w == word:
#             ways.add(way)      
#         for t in towels:
#             new_word = w + t
#             if word.startswith(new_word) and new_word not in visited:
#                 f.add((new_word, way + (t,)))
#                 visited.add((new_word, way + (t,)))
#     return ways
ways = []
for i in range(len(lines[2:])):
    if solvable[i]:
        print(i, lines[2+i])
        ways.append(words_solvable(lines[2+i], is_right=True))
print(sum(ways))