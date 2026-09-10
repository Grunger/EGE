def move(a, b):
    return (a, b + 2), (a, b * 2), (a + 2, b), (a * 2, b)


size = 100
s = [[0] * 1000 for _ in range(1000)]
win = 63  # количество камней для победы (включительно)
lose = 74 + 1  # количество камней для поражения
first = 15  # количество камней в первой куче
# где победа. Если сумма камней в требуемом диапазоне
for i in range(size):
    for j in range(size):
        if i + j in range(win, lose):
            s[i][j] = 5
# победа первым ходом. Если есть ход из неопределенной позиции в победную
for i in range(size):
    for j in range(size):
        if s[i][j] == 0 and any(s[a][b] == 5 for a, b in move(i, j)):
            s[i][j] = 1
# проигрышные позиции за 1 ход. Если все ходы ведут либо в проигрышную позицию, либо перепрыгивают
# зону победы
for i in range(size):
    for j in range(size):
        if s[i][j] == 0 and i + j < win and all(s[a][b] == 1 or a + b >= lose for a, b in move(i, j)):
            s[i][j] = -1
        # print(i, j)
# выигрышные позиции за 2 хода. Если есть ход в проигрышную позицию и она в пределах игровых позиций
for i in range(size):
    for j in range(size):
        if s[i][j] == 0 and any(s[a][b] == -1 for a, b in move(i, j)):
            s[i][j] = 2
# проигрышные позиции за 2 хода. Если все ходы либо в выигрышные позиции, либо в зону поражения
for i in range(size):
    for j in range(size):
        if s[i][j] == 0 and i + j < win and all(s[a][b] in (1, 2) or a + b >= lose for a, b in move(i, j)):
            s[i][j] = -2

# вывод начальных ситуаций
for i in range(win - first + 1):
    print(i, s[first][i])

# for i in range(size):
#     for j in range(size):
#         print(s[i][j], end='\t')
#     print()