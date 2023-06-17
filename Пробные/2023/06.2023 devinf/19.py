from functools import lru_cache


def move(x, y):
    return (2 * x, y), (x, y + 3), (x, y + 4)


@lru_cache(None)
def game(x, y):
    if (x ** 2 + y ** 2) ** 0.5 > e:
        return 5
    if any(game(a, b) == 5 for a, b in move(x, y)):
        return 1
    if all(game(a, b) == 1 for a, b in move(x, y)):
        return -1
    if any(game(a, b) == -1 for a, b in move(x, y)):
        return 2
    if all(game(a, b) > 0 for a, b in move(x, y)):
        return -2
    return 0


e = 14
for s in range(1, e):
    print(s, game(3, s))
