def move(h):
    a, b = h
    return (a + 1, b), (a + 2, b), (a + b, b), (a, b + 1), (a, b + 2), (a, b + a)


win = 150
# 61
first = 61
table = [[0] * 500 for _ in range(500)]

# win
for i in range(500):
    for j in range(500):
        if i + j >= win:
            table[i][j] = 5
# win 1
for i in range(500):
    for j in range(500):
        if table[i][j] == 0 and any(table[a][b] == 5 for a, b in move((i, j))):
            table[i][j] = 1
# lose 1
for i in range(500):
    for j in range(500):
        if table[i][j] == 0 and all(table[a][b] == 1 for a, b in move((i, j))):
            table[i][j] = -1

# win 2
for i in range(500):
    for j in range(500):
        if table[i][j] == 0 and any(table[a][b] == -1 for a, b in move((i, j))):
            table[i][j] = 2
# lose 2
for i in range(500):
    for j in range(500):
        if table[i][j] == 0 and all(table[a][b] in (1, 2) for a, b in move((i, j))):
            table[i][j] = -2
# print
for i in range(win):
    # if all(j in table[first] for j in (-2, -1, 1, 2)):
    #     print(first, 'good')
    if table[first][i] in (-2, -1, 2):
        print(i, table[first][i])


# 50 72