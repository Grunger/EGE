def move(h):
    a, b = h
    return (a, b + 1), (a, b * 2), (a + 1, b), (a * 2, b)


size = 500
s = [[0] * size for _ in range(size)]
win = 91  # количество камней для победы (включительно)
lose = 110  # количество камней для поражения
first = 40  # количество камней в первой куче
# где победа. Если сумма камней в требуемом диапазоне
for i in range(size):
    for j in range(size):
        if i + j in range(win, lose):
            s[i][j] = 5
# победа первым ходом. Если есть ход из неопределенной позиции в победную
for i in range(size):
    for j in range(size):
        if s[i][j] == 0 and any(s[a][b] == 5 for a, b in move((i, j))):
            s[i][j] = 1
# проигрышные позиции за 1 ход. Если все ходы ведут либо в проигрышную позицию, либо перепрыгивают зону победы
for i in range(size):
    for j in range(size):
        if s[i][j] == 0 and all(s[a][b] == 1 or a + b >= lose for a, b in move((i, j))):
            s[i][j] = -1
        # print(i, j)
# выигрышные позиции за 2 хода. Если есть ход в проигрышную позицию и она в пределах игровых позиций
for i in range(size):
    for j in range(size):
        if s[i][j] == 0 and any(s[a][b] == -1 and a + b < win for a, b in move((i, j))):
            s[i][j] = 2
# проигрышные позиции за 2 хода. Если все ходы либо в выигрышные позиции, либо в зону поражения
for i in range(size):
    for j in range(size):
        if s[i][j] == 0 and all(s[a][b] in (1, 2) or a + b >= lose for a, b in move((i, j))):
            s[i][j] = -2

# вывод начальных ситуаций
for i in range(win - first):
    print(i, s[first][i])
