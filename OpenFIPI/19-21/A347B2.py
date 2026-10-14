from functools import lru_cache

def m(a, b):
    return (a + 1, b), (a * 2, b), (a, b + 1), (a, b * 2)

@lru_cache(None)
def g(a, b):
    if a + b >= 107:
        return 5
    if any(g(x, y) == 5 for x, y in m(a, b)):
        return 1
    if all(g(x, y) == 1 for x, y in m(a, b)):
        return -1
    if any(g(x, y) == -1 for x, y in m(a, b)):
        return 2
    if all(g(x, y) > 0 for x, y in m(a, b)):
        return -2
    return 0

for s in range(1, 94):
    if g(13, s) == 2:
        print(s)

# 24
# 40 46
# 39 45
