from math import ceil

f = open('320_27_A.txt')
n, m = map(int, f.readline().split())
d = [0] * 1000
for line in f:
    p, k = map(int, line.split())
    k = ceil(k / 12)
    d[p] = k
max_k = 0
for p1 in range(1000):
    if d[p1] != 0:
        k = 0
        for p2 in range(1000):
            if abs(p1 - p2) <= m:
                k += d[p2]
        max_k = max(max_k, k)
print(max_k)
