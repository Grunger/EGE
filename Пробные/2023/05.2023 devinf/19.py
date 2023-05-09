from functools import lru_cache


def move(x):
    return x + 2, x + 4, x * 3


@lru_cache()
def g(x):
    if x >= 348:
        return 5
    if any(g(a) == 5 for a in move(x)):
        return 1
    if all(g(a) == 1 for a in move(x)):
        return -1
    if any(g(a) == -1 for a in move(x)):
        return 2
    if all(g(a) > 0 for a in move(x)):
        return -2
    return 0


for s in range(1, 348):
    r = g(s)
    if r == -2:
        print(s, r)
