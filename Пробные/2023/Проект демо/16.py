from functools import lru_cache


@lru_cache(None)
def f2(n):
    if n == 1:
        return 1
    return n * f(n - 1)


d = dict()


def f(n):
    if n in d:
        return d[n]
    if n == 1:
        d[1] = 1
        return 1
    d[n] = n * f(n - 1)
    return n * f(n - 1)


for i in range(1, 2024):
    print(i, f2(i))
