from math import ceil


def slow():
    max_k = 0
    for p1 in d:
        k = 0
        for p2 in d:
            if abs(p1 - p2) <= m:
                k += d[p2]
        max_k = max(max_k, k)
    return max_k


def fast():
    first = 0
    while first not in d:
        first += 1
    k = 0
    for i in range(first - m, first + m):
        if i > 0:
            k += d.get(i, 0)
    max_k = k
    for p in range(first + 1, max(d) + 1):
        if p - m in d:
            k -= d[p - m]
        if p + m in d:
            k += d[p + m]
        if p in d:
            max_k = max(k, max_k)
    return max_k


f = open('320_27_B.txt')
n, m = map(int, f.readline().split())
d = dict()
for line in f:
    p, k = map(int, line.split())
    k = ceil(k / 24)
    d[p] = k
# print(slow())
print(fast())
# 173
# 59146
