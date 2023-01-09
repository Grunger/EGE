import math

f = open('27_0.txt')
n, capacity = map(int, f.readline().split())
data = dict()
for i in range(n):
    p, k = map(int, f.readline().split())
    data[p] = math.ceil(k / capacity)
last = max(data)
m1, m2 = 0, 0
mcost = 10**10
for p1 in range(1, last):
    for p2 in range(p1 + 1, last + 1):
        cost = 0
        for p in data:
            cost += data[p] * min(abs(p1 - p), abs(p2 - p))
        if cost <= mcost:
            m1, m2 = p1, p2
            # print(f'{mcost=}, {m1=}, {m2=}')
        mcost = min(cost, mcost)
print(f'{mcost=}, {m1=}, {m2=}')
# mcost=5994, m1=82, m2=306
