from functools import lru_cache

def move(a, b):
    return (a + 1, b), (a * 2, b), (a, b + 1), (a, b * 2)


@lru_cache(None)
def game(a, b):
    if a + b >= 255:
        return 5
    if any(game(x, y) == 5 for x, y in move(a, b)):
        return 1
    if all(game(x, y) == 1 for x, y in move(a, b)):
        return -1
    if any(game(x, y) == -1 for x, y in move(a, b)):
        return 2
    if all(game(x, y) > 0 for x, y in move(a, b)):
        return -2
    return 0


for i in range(1, 238):
    if game(17, i) == -2:
        print(i, game(17, i))
