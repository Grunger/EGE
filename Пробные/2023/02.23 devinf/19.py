def move(h):
    a, b = h
    return (a + 1, b), (a + 3, b), (a * 2, b), (a, b + 1), (a, b + 3), (a, b * 2)


size = 2000
heaps = [[0] * size for _ in range(size)]
win = 479

for i in range(size):
    for j in range(size):
        if i > win or j > win:
            heaps[i][j] = 5

for i in range(size):
    for j in range(size):
        if heaps[i][j] == 0 and any(heaps[a][b] == 5 for a, b in move((i, j))):
            heaps[i][j] = 1


for i in range(size):
    for j in range(size):
        if heaps[i][j] == 0 and all(heaps[a][b] == 1 for a, b in move((i, j))):
            heaps[i][j] = -1


for i in range(size):
    for j in range(size):
        if heaps[i][j] == 0 and any(heaps[a][b] == -1 for a, b in move((i, j))):
            heaps[i][j] = 2


for i in range(size):
    for j in range(size):
        if heaps[i][j] == 0 and all(heaps[a][b] in (1, 2) for a, b in move((i, j))):
            heaps[i][j] = -2


first = 239
for i in range(win):
    if heaps[first][i] not in (0, 1):
        print(i, heaps[first][i])
