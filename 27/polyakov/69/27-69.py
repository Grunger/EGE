# Автор: В. Ярцев

from itertools import combinations as cmb
from operator import xor
s = [0]
with open('27-69b.txt') as f:
    N = int(f.readline())
    for _ in range(N):
        a = [int(n) for n in f.readline().split()]
        t = [x + y + z for x in s for y, z in cmb(a, r=2)]
        s = {(x % 7, x % 10): x for x in sorted(t)}.values()
print(max(x for x in s if xor(x % 7 == 3, x % 10 == 5)))
