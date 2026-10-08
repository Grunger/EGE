from itertools import *
a, x, F = [[1000000000] * 5 for i in range(9)], [],open('27-57b.txt','r')
for i in range(int(F.readline())):
    c = int(F.readline())
    d = c % 9
    a[d][4] = c
    a[d].sort()
for i in a:
    for j in i[:4]: x.append(j)
print(min([sum(i) for i in permutations(x, 4) if sum(i) % 9 == 0]))
