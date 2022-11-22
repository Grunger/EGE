def moves(a, b):
    return (a + 1, b), (a * 2, b), (a, b + 1), (a, b * 2)


win = 107
first = 13
s = [[0 for i in range(1000)] for j in range(1000)]

for i in range(500):
    for j in range(500):
        if i + j >= win:
            s[i][j] = 5
for i in range(win):
    for j in range(win):
        if s[i][j] == 0 and any(s[a][b] == 5 for a, b in moves(i, j)):
            s[i][j] = 1
for i in range(win):
    for j in range(win):
        if s[i][j] == 0 and all(s[a][b] == 1 for a, b in moves(i, j)):
            s[i][j] = -1
for i in range(win):
    for j in range(win):
        if s[i][j] == 0 and any(s[a][b] == -1 for a, b in moves(i, j)):
            s[i][j] = 2
for i in range(win):
    for j in range(win):
        if s[i][j] == 0 and all(s[a][b] in (1, 2) for a, b in moves(i, j)):
            s[i][j] = -2
for i in range(win + 1):
    if s[first][i]:
        print(i, s[first][i])

# 24