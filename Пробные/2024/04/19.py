from functools import lru_cache

def move(a, b):
    return (a + 1, b), (a * 2, b), (a, b + 1), (a, b * 2)


@lru_cache(None)
def g(a, b):
    if a + b >= 255:
        return 5
    if any(g(i, j) == 5 for i, j in move(a, b)):
        return 1
    # 19 задание неудачный ход all -> any
    if any(g(i, j) == 1 for i, j in move(a, b)):
        return -1
    if any(g(i, j) == -1 for i, j in move(a, b)):
        return 2
    if all(g(i, j) in (1, 2) for i, j in move(a, b)):
        return -2

for s in range(1, 238):
    if g(21, s) == -1:
        print(s, g(21, s))

