def move(h):
    a, b = h
    return (a + b, b), (a, a + b)


s = [[0] * 1000 for _ in range(1000)]
win = 29
first = 5
for i in range(500):
    for j in range(500):
        if i + j >= win:
            s[i][j] = 5
for i in range(500):
    for j in range(500):
        if s[i][j] == 0 and any(s[a][b] == 5 for a, b in move((i, j))):
            s[i][j] = 1

for i in range(500):
    for j in range(500):
        if s[i][j] == 0 and all(s[a][b] == 1 for a, b in move((i, j))):
            s[i][j] = -1

for i in range(500):
    for j in range(500):
        if s[i][j] == 0 and any(s[a][b] == -1 for a, b in move((i, j))):
            s[i][j] = 2

for i in range(500):
    for j in range(500):
        if s[i][j] == 0 and all(s[a][b] in (1, 2) for a, b in move((i, j))):
            s[i][j] = -2
for i in range(win + 1):
    if s[first][i] in (-2, -1, 2, 1):
        print((first, i), s[first][i])

