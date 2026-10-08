from functools import lru_cache

# @lru_cache(None)
def f(n):
    global k
    k += 1
    if n <= 2:
        return 2
    return f(n - 1) - 2 * f(n - 2)


k = 0
f(57)
print(k)
