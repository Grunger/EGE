from math import ceil

f = open('220_27_A.txt')
n = int(f.readline())
d = dict()
for line in f:
    p, k = map(int, line.split())
    k = ceil(k / 36)
    d[p] = k
min_cost = 10 ** 9
for p1 in d:
    cost = 0
    for p2 in d:
        cost += d[p2] * abs(p2 - p1)
    min_cost = min(min_cost, cost)
print(min_cost)
