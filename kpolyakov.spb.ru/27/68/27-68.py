from itertools import combinations as cmb
from operator import xor
k = 3
p = 17
s = [0]
with open('27-68b.txt') as f:
    N = int(f.readline())
    for _ in range(N):
        a = [int(n) for n in f.readline().split()]
        t = [x + y + z for x in s for y, z in cmb(a, r=2)]
        s = {(x % k, x % p): x for x in sorted(t, reverse=True)}.values()
print(min( x for x in s if xor(x % k == 0, x % p == 0)))