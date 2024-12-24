import sys
lines = [i.strip() for i in open(sys.argv[1]).readlines()]
# line = open(sys.argv[1]).read()

regs = [i for i in lines if ':' in i]
settings = {(i[i.find(' -> ')+4:].strip()):tuple(i[:i.find(' -> ')].split(' ')) for i in lines if '->' in i}

registers = {i[:i.find(':')]:int(i[i.find(':')+1:]) for i in regs}


solvable_order = sorted(list(registers))
# part 1
solvable = {i for i in settings if settings[i][0] in registers and settings[i][2] in registers and i not in registers}
while len(solvable):
    solvable_order.extend(sorted(solvable))
    print(sorted(solvable))
    for i in solvable:
        if settings[i][1]=='AND':
            registers[i] = registers[settings[i][0]] & registers[settings[i][2]]
        elif settings[i][1]=='XOR':
            registers[i] = registers[settings[i][0]] ^ registers[settings[i][2]]
        elif settings[i][1]=='OR':
            registers[i] = registers[settings[i][0]] | registers[settings[i][2]]
    solvable = {i for i in settings if settings[i][0] in registers and settings[i][2] in registers and i not in registers}
for i in sorted(registers):
    print(i,registers[i])


z_regs = sorted([(i,str(registers[i])) for i in registers if i.startswith('z')],reverse=True)
print(int(''.join([i[1] for i in z_regs]),2))


# part 2
print(len(registers))

# iterate through all the x registers and 




# swapped outputs
swaps = set()

x_regs = sorted([(i,str(registers[i])) for i in registers if i.startswith('x')],reverse=True)
y_regs = sorted([(i,str(registers[i])) for i in registers if i.startswith('y')],reverse=True)
expected = int(''.join([i[1] for i in x_regs]),2) + int(''.join([i[1] for i in y_regs]),2)
expected_bin = bin(expected)[2:]
# build the actual thing and show specifically where it doesn't work?
print(expected_bin)
print(''.join(i[1] for i in z_regs))
for n,i in enumerate(z_regs):
    if i[1]!=expected_bin[n]:
        print(i[0])

# # padding extra y registers
# if len(x_regs) > len(y_regs):
#     for i in range(int(y_regs[-1][1:]),int(x_regs[-1][1:])+1):
#         registers[i][]

# import itertools
# c = itertools.combinations(settings.keys(), 2)
# for i in itertools.combinations(c, 4):
#     if len(set(sum(i,start = tuple()))) == 8:
#         dummy_set = settings.copy()
#         dummy_regs = registers.copy()
#         # make swaps
#         for j in i:
#             dummy_set[j[0]] = settings[j[1]]
#             dummy_set[j[1]] = settings[j[0]]

#         # run process
#         solvable = {i for i in dummy_set if dummy_set[i][0] in dummy_regs and dummy_set[i][2] in dummy_regs and i not in dummy_regs}
#         while len(solvable):
#             for i in solvable:
#                 if dummy_set[i][1]=='AND':
#                     dummy_regs[i] = dummy_regs[dummy_set[i][0]] & dummy_regs[dummy_set[i][2]]
#                 elif dummy_set[i][1]=='XOR':
#                     dummy_regs[i] = dummy_regs[dummy_set[i][0]] ^ dummy_regs[dummy_set[i][2]]
#                 elif dummy_set[i][1]=='OR':
#                     dummy_regs[i] = dummy_regs[dummy_set[i][0]] | dummy_regs[dummy_set[i][2]]
#             solvable = {i for i in dummy_set if dummy_set[i][0] in dummy_regs and dummy_set[i][2] in dummy_regs and i not in dummy_regs}
#         z_regs = sorted([(i,str(registers[i])) for i in registers if i.startswith('z')],reverse=True)
#         if int(''.join([i[1] for i in z_regs]),2) == expected:
#             print(sorted(sum(i, start = tuple())))
print(expected)

class BstNode:

    def __init__(self, key):
        self.key = key
        self.right = BstNode(max(settings[key][2],settings[key][0])) if key in settings else None
        self.left = BstNode(min(settings[key][2],settings[key][0])) if key in settings else None
        self.m = settings[key][1] if key in settings else ''

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % str(self.key)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % str(self.key)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % str(self.key)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = self.m + '%s' % str(self.key)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

b = BstNode(solvable_order[-1])
# b.display()

examine = {BstNode(i) for i in registers if i.startswith('z')}
s = set()
while len(examine):
    i = examine.pop()
    if i:
        # if not ( or 
        #         (i.m == 'OR' and {i.left.m, i.right.m} == {'AND'} and 'x00' not in {i.left.left.key, i.right.left.key,i.left.right.key, i.right.right.key}) or
        #         (i.m == 'XOR' and {i.key[0]  in 'xyz' or i.left.key[0]  in 'xyz' or i.right.key[0]  in 'xyz'}) or 
        #         (i.m == 'AND' and ({i.left.m, i.right.m} == {'XOR', 'OR'} or {i.left.m, i.right.m} == {''})) or
        #         i.m == ''):
        if (i.key.startswith('z') and i.m != 'XOR' and i.key!=max(registers)):
            s.add((i.key, i.m, (i.left.m, i.right.m)))
        elif (i.m == 'XOR' and i.key[0] not in 'xyz' and i.left.key[0] not in 'xyz' and i.right.key[0] not in 'xyz'):
            s.add((i.key, i.m, (i.left.m, i.right.m)))
        elif i.m == 'OR' and {i.left.m, i.right.m} != {'AND'}:
            if i.left.m != 'AND':
                s.add((i.left.key, i.left.m, (i.left.left.m, i.left.right.m)))
            if i.right.m != 'AND':
                s.add((i.right.key, i.right.m, (i.right.left.m, i.right.right.m)))
        elif i.m == 'AND' and 'AND' in {i.left.m, i.right.m}:
            if i.left.m == 'AND' and i.left.left.key != 'x00':
                s.add((i.left.key, i.left.m, (i.left.left.m, i.left.right.m)))
            if i.right.m == 'AND' and i.right.left.key != 'x00':
                s.add((i.right.key, i.right.m, (i.right.left.m, i.right.right.m)))
        examine.add(i.left)
        examine.add(i.right)

print(sorted(s))
print(','.join(sorted([i[0] for i in s])))
