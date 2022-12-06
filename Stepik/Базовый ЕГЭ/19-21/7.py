def move(h):
    a, b = h
    return (a + 1, b), (a * 3, b), (a, b + 1), (a, b * 3)


s = [[0] * 1000 for _ in range(1000)]
win = 100
for first in range(win):
    for i in range(1000):
        for j in range(1000):
            if i >= win or j >= win:
                s[i][j] = 5
    for i in range(1000):
        for j in range(1000):
            if s[i][j] == 0 and any(s[a][b] == 5 for a, b in move((i, j))):
                s[i][j] = 1

    for i in range(1000):
        for j in range(1000):
            if s[i][j] == 0 and all(s[a][b] == 1 for a, b in move((i, j))):
                s[i][j] = -1

    for i in range(1000):
        for j in range(1000):
            if s[i][j] == 0 and any(s[a][b] == -1 for a, b in move((i, j))):
                s[i][j] = 2

    for i in range(1000):
        for j in range(1000):
            if s[i][j] == 0 and all(s[a][b] in (1, 2) for a, b in move((i, j))):
                s[i][j] = -2
    if all(i in s[first] for i in (-1, -2, 2)):
        print(first)
        for i in range(183 + 1):
            if s[first][i] in (-2, -1, 2):
                print((first, i), s[first][i])
        print('-' * 10)
