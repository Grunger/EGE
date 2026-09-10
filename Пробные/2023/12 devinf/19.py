def move(h):
    a, b = h
    return (a + b, b), (a, a + b)


s = [[0] * 500 for _ in range(500)]
win = 212
size = 500
for i in range(size):
    for j in range(size):
        if i + j >= win:
            s[i][j] = 5
for i in range(size):
    for j in range(size):
        if s[i][j] == 0 and any(s[a][b] == 5 for a, b in move((i, j))):
            s[i][j] = 1
for i in range(size):
    for j in range(size):
        if s[i][j] == 0 and all(s[a][b] == 1 for a, b in move((i, j))):
            s[i][j] = -1
for i in range(size):
    for j in range(size):
        if s[i][j] == 0 and any(s[a][b] == -1 for a, b in move((i, j))):
            s[i][j] = 2
for i in range(size):
    for j in range(size):
        if s[i][j] == 0 and all(s[a][b] == 2 for a, b in move((i, j))):
            s[i][j] = -2

for i in range(size):
    if s[10][i] == -2:  # 29-38 71-80
        print(i)
# 19
# 100 11 -> 100 111 = 211

# 20
# 50 37 -> 87 37