def move(n):
    return [n[0], n[1] + 1], [n[0], n[1] + 2], [n[0], n[1] * 2], [n[0] + 1, n[1]], [n[0] + 2, n[1]], [n[0] * 2, n[1]]


s = [[0] * 500 for _ in range(500)]
first = 24  # количество камней в первой куче 24 21
win = 50  # количество камней для победы
lose = 109  # количество камней для поражения

# где победа. Если сумма камней в требуемом диапазоне
for i in range(500):
    for j in range(500):
        if (i >= win or j >= win) and i + j < lose:
            s[i][j] = 5
# победа первым ходом. Если есть ход из неопределенной позиции в победную
for i in range(win):
    for j in range(win):
        if s[i][j] == 0 and any(s[a][b] == 5 for a, b in move((i, j))):
            s[i][j] = 1
# проигрышные позиции за 1 ход. Если все ходы ведут либо в проигрышную позицию, либо перепрыгивают зону победы
for i in range(win):
    for j in range(win):
        if s[i][j] == 0 and all(s[a][b] == 1 or a + b >= lose for a, b in move((i, j))):
            s[i][j] = -1
        # print(i, j)
# выигрышные позиции за 2 хода. Если есть ход в проигрышную позицию и она в пределах игровых позиций
for i in range(win):
    for j in range(win):
        if s[i][j] == 0 and any(s[a][b] == -1 for a, b in move((i, j))):
            s[i][j] = 2
# проигрышные позиции за 2 хода. Если все ходы либо в выигрышные позиции, либо в зону поражения
for i in range(win):
    for j in range(win):
        if s[i][j] == 0 and all(s[a][b] in (1, 2) or a + b >= lose for a, b in move((i, j))):
            s[i][j] = -2
# вывод начальных ситуаций
for i in range(12, win):
    print(i, s[first][i])
print(-2 in s[first][12:win])
