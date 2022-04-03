f = open('5_27_B.txt')
n = int(f.readline())
s = []
r = 17
m = 0
for i in range(n):
    x = int(f.readline())
    s.extend([x + a for a in s] + [x])
    s = {x % r: x for x in sorted(s)}
    s = list(s.values())
print(max(i for i in s if i % r == 0))
