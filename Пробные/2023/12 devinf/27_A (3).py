import math

f = open('27_0.txt')
n, capacity = map(int, f.readline().split())
data = dict()
for i in range(n):
    p, k = map(int, f.readline().split())
    data[p] = math.ceil(k / capacity)
last = max(data)
min_cost = 10**10
for p1 in range(last + 1):
    print(p1, last)
    cost = 0
    for i in range(last + 1):
        cost += abs(p1 - i) * data.get(i, 0)
    min_cost = min(cost, min_cost)
print(min_cost)
# 18
# 14366
