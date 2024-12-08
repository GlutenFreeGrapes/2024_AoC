map = [i.strip() for i in open('input.txt').readlines()]
ROWS, COLS = len(map), len(map[0])

freqs_to_locations = {}
for n,i in enumerate(map):
    for j in range(COLS):
        if i[j]!='.':
            if i[j] in freqs_to_locations:
                freqs_to_locations[i[j]].add((n,j))
            else:
                freqs_to_locations[i[j]] = {(n,j)}
print(freqs_to_locations)

import itertools, numpy as np
# part 1
antinodes = set()
for i in freqs_to_locations:
    # every pair of nodes
    for j1, j2 in itertools.combinations(freqs_to_locations[i], 2):
        diff = np.subtract(j2, j1)
        a1 = np.subtract(j1, diff)
        a2 = np.add(j2, diff)
        if (0 <= a1[0] < ROWS) and (0 <= a1[1] < COLS):
            antinodes.add(tuple(a1))
        if (0 <= a2[0] < ROWS) and (0 <= a2[1] < COLS):
            antinodes.add(tuple(a2))
print(len(antinodes))

# part 2
antinodes = set()
for i in freqs_to_locations:
    # every pair of nodes
    for j1, j2 in itertools.combinations(freqs_to_locations[i], 2):
        diff = np.subtract(j2, j1)
        # make diff the gcd of its coordinates
        # diff = diff / np.gcd.reduce(diff)

        a1 = j1
        while (0 <= a1[0] < ROWS) and (0 <= a1[1] < COLS):
            antinodes.add(tuple(a1))
            a1 = np.subtract(a1, diff)

        a2 = j2
        while (0 <= a2[0] < ROWS) and (0 <= a2[1] < COLS):
            antinodes.add(tuple(a2))
            a2 = np.add(a2, diff)
# print(antinodes)
print(len(antinodes))