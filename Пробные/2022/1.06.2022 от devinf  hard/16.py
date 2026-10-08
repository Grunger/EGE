from functools import lru_cache

@lru_cache(None)
def f(n):
    if n <= 2:
        return 1
    return f(n - 1) + f(n - 2) + 1


print(f(57))
