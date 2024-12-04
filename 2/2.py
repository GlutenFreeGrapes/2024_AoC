inputs = []

c = 0
for i in open('input.txt','r').readlines():
    l = [int(j) for j in i.split()]
    inputs.append(l)
    
def safe(l):
    # check all increasing/decreasing
    if l[0] < l[-1]:
        s=False
    elif l[0] > l[-1]:
        s=True
    else:
        return False
    if sorted(l, reverse=s) == l:
        # check gradual
        p = True
        for j in range(len(l)-1):
            p = p and (abs(l[j+1] - l[j]) <= 3 and l[j+1]!=l[j])
        return p
    return False

err = []

# part 1
for l in inputs:
    if safe(l):
        c+=1
    else:
        err.append(l)
print(c)

# part 2
for l in err:
    for j in range(len(l)):
        if safe(l[:j]+l[j+1:]):
            c+=1
            break
print(c)