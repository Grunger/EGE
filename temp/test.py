def move(x, last):
    if last == 1:
        return (x + 6, 2), (x * 2, 3)
    elif last == 2:
        return (x + 3, 1), (x * 2, 3)
    elif last == 3:
        return (x + 3, 1), (x + 6, 2)
    return (x + 3, 1), (x + 6, 2), (x * 2, 3)


def game(p, last):
    if p > 40:
        return 5
    if any(game(x, k) == 5 for x, k in move(p, last)):
        return 1
    if all(game(x, k) == 1 for x, k in move(p, last)):
        return -1
    if any(game(x, k) == -1 for x, k in move(p, last)):
        return 2
    if all(game(x, k) > 0 for x, k in move(p, last)):
        return -2
    return 0


for i in range(1, 37):
    print(i, game(i, 0))
