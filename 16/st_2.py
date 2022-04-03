from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 1:
        return 2
    return (2 * g(n - 1) + f(n - 1)) // 2


@lru_cache(None)
def g(n):
    if n <= 1:
        return 1
    return 2 * f(n - 1) // 3 + g(n - 1)


for i in range(1, 100):
        print(i, f(i), g(i))
