from functools import lru_cache

def m(a, b):
    return (a + 3, b), (a * 3, b), (a, b + 3), (a, b * 3)

@lru_cache(None)
def g(a, b):
    if a + b >= 176:
        return 5
    if any(g(x, y) == 5 for x, y in m(a, b)):
        return 1
    if any(g(x, y) == 1 for x, y in m(a, b)):
        return -1
    if any(g(x, y) == -1 for x, y in m(a, b)):
        return 2
    if all(g(x, y) > 0 for x, y in m(a, b)):
        return -2
    return 0

for s in range(1, 162):
    if g(14, s) == -1:
        print(s)