import math
from itertools import accumulate

f = open('27_B.txt')
n, capacity = map(int, f.readline().split())
data = dict()
for i in range(n):
    p, k = map(int, f.readline().split())
    data[p] = math.ceil(k / capacity)
last = max(data)
for i in range(last):
    if i not in data:
        data[i] = 0
data = {i: data[i] for i in sorted(data)}

pref = [0] * (last * 2 + 1)
post = [0] * (last * 2 + 1)
for i, k in enumerate(accumulate(data.values())):
    post[i] = k
data1 = {i: data[i] for i in list(data)[::-1]}
for i, k in enumerate(list(accumulate(data1.values()))[::-1]):
    pref[i] = k
pref.pop(0)

cost = 0
for i in range(last + 1):
    cost += (i - 1) * data[i]
min_cost = cost
for i in range(1, last + 1):
    cost += post[i] - pref[i]
    min_cost = min(min_cost, cost)
print(min_cost)
