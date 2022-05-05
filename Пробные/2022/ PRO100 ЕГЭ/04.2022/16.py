from functools import lru_cache


@lru_cache()
def f(n):
    if n == 0:
        return 1
    return f(n - 1) * n


for i in range(100):
    print(i, f(i))
