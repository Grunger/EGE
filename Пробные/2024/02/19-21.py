from functools import lru_cache


def move(x):
    return x + 1, x + 2, x * 3


@lru_cache(None)
def g(s):
    if s >= win:
        return 5
    if any(g(i) == 5 for i in move(s)):
        return 1
    if all(g(i) == 1 for i in move(s)):
        return -1
    if any(g(i) == -1 for i in move(s)):
        return 2
    if all(g(i) in (1, 2) for i in move(s)):
        return -2


win = 212
for i in range(1, win + 1):
    if g(i) in (-2, -1, 2):
        print(i, g(i))
