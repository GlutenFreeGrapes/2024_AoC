import re
inputs=open('input.txt').read()
# inputs= "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
# part 1
s = 0
for i in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', inputs):
    s+=(int(i[0])*int(i[1]))
print(s)

s = 0
for m in re.findall(r"do\(\)(.*?)(?=don't\(\))", 'do()'+inputs+"don't()", re.DOTALL):
    for i in re.findall(r'mul\((\d+),(\d+)\)', m):
        s+=(int(i[0])*int(i[1]))
print(s)