from functools import lru_cache

def m(a):
    return a + 1, a * 2

@lru_cache(None)
def g(a):
    if a >= 49:
        return 5
    if any(g(x) == 5 for x in m(a)):
        return 1
    if all(g(x) == 1 for x in m(a)):
        return -1
    if any(g(x) == -1 for x in m(a)):
        return 2
    if all(g(x) > 0 for x in m(a)):
        return -2
    return 0

for s in range(1, 49):
    if g(s) == -2:
        print(s)