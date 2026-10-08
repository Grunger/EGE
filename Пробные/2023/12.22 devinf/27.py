from math import ceil

f = open('27_A.txt')
n, m = map(int, f.readline().split())
d = dict()
for s in f:
    p, c = map(int, s.split())
    d[p] = ceil(c / m)
min_cost = 10**9
for p1 in range(max(d)):
    cost = 0
    for p in d:
        cost += abs(p - p1) * d[p]
    min_cost = min(min_cost, cost)
print(min_cost)

