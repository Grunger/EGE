import sys

a = sys.stdin.read().strip().split('\n')
a = [[int(i) for i in s.split()] for s in a]
# a = a[:10]
k = 0
for s in a:
    c = [s.count(i) for i in s]
    r = [i for i in s if s.count(i) > 1]
    n = [i for i in s if s.count(i) == 1]
    if c.count(3) == 3 and c.count(1) == 3:
        if r[0] ** 2 * 3 > sum(i**2 for i in n):
            k += 1
    # print(s, c, r, n, k)
print(k)