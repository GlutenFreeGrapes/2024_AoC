l1, l2 = [], []
for i in open('input.txt','r').readlines():
    n = i.strip().split(' ')
    l1.append(int(n[0]))
    l2.append(int(n[1]))
# part 1
l1=sorted(l1)
l2=sorted(l2)
d=0
for i in range(len(l1)):
    d+=abs(l1[i]-l2[i])
print(d)

# part 2
s = 0
for i in l1:
    s += i*l2.count(i)
print(s)