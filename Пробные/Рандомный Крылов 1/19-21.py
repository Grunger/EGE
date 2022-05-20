def move(h):
    a, b = h
    return (a + 1, b), (a * 2, b), (a, b + 1), (a, b * 2)


pos = []
for i in range(300):
    row = []
    for j in range(300):
        row.append(0)
    pos.append(row)

for i in range(113 + 1):
    for j in range(113 + 1):
        if any(sum(h) >= 123 for h in move((i, j))):
            # print(i , j)
            pos[i][j] = 1
for i in range(113 + 1):
    for j in range(113 + 1):
        if pos[i][j] == 0 and all(pos[a][b] == 1 for a, b in move((i, j))):
            pos[i][j] = -1
for i in range(113 + 1):
    for j in range(113 + 1):
        if pos[i][j] == 0 and any(pos[a][b] == -1 for a, b in move((i, j))):
            pos[i][j] = 2
for i in range(113 + 1):
    for j in range(113 + 1):
        if pos[i][j] == 0 and all(pos[a][b] in (1, 2) for a, b in move((i, j))):
            pos[i][j] = -2
print(*list(enumerate(pos[9][:58 + 1])), sep='\n')
