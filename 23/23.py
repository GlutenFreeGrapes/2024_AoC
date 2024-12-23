import sys
lines = [i.strip() for i in open(sys.argv[1]).readlines()]
# line = open(sys.argv[1]).read()

class Computer():
    def __init__(self, name):
        self.name = name
        self.neighbors = set()
        self.neighbors_names = set()
    def add_neighbor(self, c):
        self.neighbors.add(c)
        self.neighbors_names.add(c.name)

        
computer_names = {}
for i in lines:
    comps = i.split('-')
    if comps[0] not in computer_names:
        computer_names[comps[0]] = Computer(comps[0])
    if comps[1] not in computer_names:
        computer_names[comps[1]] = Computer(comps[1])
    computer_names[comps[1]].add_neighbor(computer_names[comps[0]])
    computer_names[comps[0]].add_neighbor(computer_names[comps[1]])
print(len(computer_names))    

# part 1
sets_of_3 = set()
for i in computer_names:
    for j in computer_names[i].neighbors:
        if i!=j.name:
            for k in computer_names[i].neighbors.intersection(computer_names[j.name].neighbors):
                if k.name!=i and k.name!=j.name:
                    sets_of_3.add(tuple(sorted((i,j.name,k.name))))
print(len({i for i in sets_of_3 if any({j.startswith('t') for j in i})}))

# part 2
maxc = -1
for k in computer_names:
    clique = [computer_names[k]]
    for i in computer_names:
        if all({i in j.neighbors_names for j in clique}):
            clique.append(computer_names[i])
    if len(clique) > maxc:
        maxc = len(clique)
        print(maxc, ','.join(sorted([i.name for i in clique])))
print(maxc)