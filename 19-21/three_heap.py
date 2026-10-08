def moves(h):
    a, b, c = h
    return (a + 1, b, c), (a * 2, b, c), (a, b + 1, c), (a, b * 2, c), (a, b, c + 1), (a, b, c * 2)


s = [[[0] * 500 for _ in range(500)] for _ in range(500)]
win = 60
first = 20
second = 10

for i in range(win):
    for j in range(win):
        for k in range(win):
            if i + j + k >= win:
                s[i][j][k] = 5

for i in range(win):
    for j in range(win):
        for k in range(win):
            if s[i][j][k] == 0 and any(s[a][b][c] == 5 for a, b, c in moves((i, j, k))):
                s[i][j][k] = 1

for i in range(win):
    for j in range(win):
        for k in range(win):
            if s[i][j][k] == 0 and all(s[a][b][c] == 1 for a, b, c in moves((i, j, k))):
                s[i][j][k] = -1

for i in range(win):
    for j in range(win):
        for k in range(win):
            if s[i][j][k] == 0 and any(s[a][b][c] == -1 for a, b, c in moves((i, j, k))):
                s[i][j][k] = 2

for i in range(win):
    for j in range(win):
        for k in range(win):
            if s[i][j][k] == 0 and all(s[a][b][c] in (1, 2) for a, b, c in moves((i, j, k))):
                s[i][j][k] = -2


for i in range(win):
    print(i, s[first][second][i])
