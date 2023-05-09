from functools import lru_cache
from sys import setrecursionlimit

f = [0] * 5000
for n in range(4000, 0, -1):
    if n > 3000:
        f[n] = n
    elif n % 2 == 0:
        f[n] = n + f[n + 1] + 1
    else:
        f[n] = f[n + 2] + 2
print(f[40] - f[43])


@lru_cache()
def f(n):
    if n > 3000:
        return n
    if n % 2 == 0:
        return n + f(n + 1) + 1
    return f(n + 2) + 2


setrecursionlimit(5000)
print(f(40) - f(43))
