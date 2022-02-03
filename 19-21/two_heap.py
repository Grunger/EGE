def moves(h):
    a, b = h
    return (a + 3, b), (a * 2, b), (a, b + 3), (a, b * 2)


s = [[0] * 500 for _ in range(500)]
win = 157
first = 43
for i in range(win):
    for j in range(win):
        if i + j >= win:
            s[i][j] = 5

for i in range(win):
    for j in range(win):
        if s[i][j] == 0 and any(s[i][j] == 5 for i, j in moves((i, j))):
            s[i][j] = 1

for i in range(win):
    for j in range(win):
        if s[i][j] == 0 and all(s[i][j] == 1 for i, j in moves((i, j))):
            s[i][j] = -1

for i in range(win):
    for j in range(win):
        if s[i][j] == 0 and any(s[i][j] == -1 for i, j in moves((i, j))):
            s[i][j] = 2

for i in range(win):
    for j in range(win):
        if s[i][j] == 0 and all(s[i][j] in (1, 2) for i, j in moves((i, j))):
            s[i][j] = -2

for i in range(win - first):
    print(i, s[first][i])
