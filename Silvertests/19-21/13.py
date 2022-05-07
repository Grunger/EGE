def moves(h):
    a, b = h
    return (a + 3, b), (a * 2, b), (a, b + 3), (a, b * 2)


s = [[0] * 1000 for _ in range(1000)]
win = 50
first = 23
for i in range(1000):
    for j in range(1000):
        if i >= win or j >= win:
            s[i][j] = 5

for i in range(1000):
    for j in range(1000):
        if s[i][j] == 0 and any(s[a][b] == 5 for a, b in moves((i, j))):
            s[i][j] = 1

for i in range(1000):
    for j in range(1000):
        if s[i][j] == 0 and all(s[a][b] == 1 for a, b in moves((i, j))):
            s[i][j] = -1

for i in range(1000):
    for j in range(1000):
        if s[i][j] == 0 and any(s[a][b] == -1 for a, b in moves((i, j))):
            s[i][j] = 2

for i in range(1000):
    for j in range(1000):
        if s[i][j] == 0 and all(s[a][b] in (1, 2) for a, b in moves((i, j))):
            s[i][j] = -2

for i in range(win - first):
    print(i, s[first][i])
