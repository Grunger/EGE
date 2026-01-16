from functools import lru_cache

@lru_cache(None)
def f(a, b):
    if a < b or a == 7:
        return 0
    if a == b:
        return 1
    return f(a - 1, b) + f(a - 2, b) + f(a // 3, b)



print(f(15, 8) * f(8, 3))
