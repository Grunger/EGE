from functools import lru_cache

def m(a, b):
    return (a + 4, b), (a * 2, b), (a, b + 4), (a, b * 2)

@lru_cache(None)
def g(a, b):
    if a + b >= 133:
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

for s in range(1, 116):
    if g(17, s) == -2:
        print(s)