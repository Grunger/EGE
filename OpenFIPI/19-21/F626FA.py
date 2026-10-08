from functools import lru_cache

def m(a, b):
    return (a + 1, b), (a * 3, b), (a, b + 1), (a, b * 3)

@lru_cache(None)
def g(a, b):
    if a + b >= 155:
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

for s in range(1, 140):
    if g(15, s) == -1:
        print(s)