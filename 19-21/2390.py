# 2 кучи
# +1 *2
# 4, 1 <= s <= 40
# win 45


def turn(x, y):
    return (x + 1, y), (x * 2, y), (x, y + 1), (x, y * 2)


def win(h):
    return sum(h) >= 75


s = 67
pos = []
for i in range(500):
    row = []
    for j in range(500):
        row.append(0)
    pos.append(row)
# pos = [[0 for _ in range(500)] for _ in range(500)]

# победа в 1 ход
for x in range(s):
    for y in range(s):
        if any(win(h) for h in turn(x, y)):
            pos[x][y] = 1

# поражение в 1 ход
for x in range(s):
    for y in range(s):
        if pos[x][y] == 0:
            if all(pos[h[0]][h[1]] == 1 for h in turn(x, y)):
                pos[x][y] = -1

# победа в 2 хода
for x in range(s):
    for y in range(s):
        if pos[x][y] == 0:
            if any(pos[h[0]][h[1]] == -1 for h in turn(x, y)):
                pos[x][y] = 2

# поражение в 2 хода
for x in range(s):
    for y in range(s):
        if pos[x][y] == 0:
            if all(pos[h[0]][h[1]] in (1, 2) for h in turn(x, y)):
                pos[x][y] = -2

print(*enumerate(pos[8][:s]), sep='\n')
