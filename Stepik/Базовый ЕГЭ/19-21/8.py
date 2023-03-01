def move(h):
    a, b = h
    return (a + 2, b), (a * 2, b), (a, b + 2), (a, b * 2)


s = [[0] * 1000 for _ in range(1000)]
win = 67
lose = 82
first = 25
for i in range(500):
    for j in range(500):
        if lose >= i + j >= win:
            s[i][j] = 5
for i in range(500):
    for j in range(500):
        if s[i][j] == 0 and any(s[a][b] == 5 for a, b in move((i, j))):
            s[i][j] = 1

for i in range(500):
    for j in range(500):
        if s[i][j] == 0 and all(s[a][b] == 1 or a + b > lose for a, b in move((i, j))):
            s[i][j] = -1

for i in range(500):
    for j in range(500):
        if s[i][j] == 0 and any(s[a][b] == -1 for a, b in move((i, j))):
            s[i][j] = 2

for i in range(500):
    for j in range(500):
        if s[i][j] == 0 and all(s[a][b] in (1, 2) or a + b > lose for a, b in move((i, j))):
            s[i][j] = -2

for i in range(38):
    if s[first][i] in (-2, -1, 2):
        print((first, i), s[first][i])
print('-' * 10)
