from string import ascii_uppercase

field = [[0] * 30 for _ in range(1010)]
f = open('26.txt')
n = int(f.readline())
# Заполнение занятых точек единицами
for i in range(n):
    col, row = f.readline().split()
    row = int(row)
    col = ascii_uppercase.index(col)
    field[row][col] = 1

# точка пожара
col, row = f.readline().split()
row = int(row)
col = ascii_uppercase.index(col)
fire = [row, col]

# поиск всех подходящих под посадку мест.
good = []
for i in range(2, 997):
    for j in range(2, 24):
        a = (-2, -1, 0, 1, 2)
        g = True
        for c in a:
            for d in a:
                if field[i + c][j + d] == 1:
                    g = False
        if g:
            good.append((i, j))
print(len(good))

# поиск ближайшей к точке пожара зоне высадки.
m = 10**9
for x, y in good:
    d = ((x - fire[0]) ** 2 + (y - fire[1]) ** 2) ** 0.5
    # print(ascii_uppercase[y], x, d**0.5)
    if d < m:
        m = d
        ans = (x, y)
print(ascii_uppercase[ans[1]], ans[0], m)
# D 506
