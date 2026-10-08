def move(h):
    a, b = h
    return (a + 1, b), (a * 2, b), (a, b + 1), (a, b * 2)


s = [[0] * 1000 for _ in range(1000)]
win = 255
first = 17
for i in range(1000):
    for j in range(1000):
        if i + j >= win:
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

for i in range(238 + 1):
    if s[first][i] in (-2, -1, 2):
        print((first, i), s[first][i])
