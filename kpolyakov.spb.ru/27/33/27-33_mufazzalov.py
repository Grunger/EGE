# Автор: Д. Муфаззалов

from itertools import *

f = open("27-33b.txt")
s= [0]
for _ in range(int(f.readline())):
    a = list(map(int, f.readline().split()))
    t = sorted([i + sum(x) for i in s for x in combinations(a, r=2)])
    s = {(i % 4): i for i in t}.values()
print(*[i for i in s if i % 4 == 0])
