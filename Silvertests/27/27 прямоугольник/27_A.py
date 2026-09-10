f = open('27A.txt')
size_x, size_y = map(int, f.readline().split())
n = int(f.readline())
dots = [(0, 0), (0, size_y), (size_x, 0), (size_x, size_y)]
for i in range(n):
    x, y = map(int, f.readline().split())
    dots.append((x, y))
ms = 0
mp = 0
# перебираем все пары точек и смотрим, есть
# ли между ними еще точки
for x in range(size_x):
    for y in range(size_y):
        for x_end in range(x, size_x):
            for y_end in range(y, size_y):
                good = True
                for c in dots:
                    if x < c[0] < x_end and y < c[1] < y_end:
                        good = False
                        break
                # если точек нет - можно построить прямоугольник
                if good:
                    s = (x_end - x) * (y_end - y)
                    p = 2 * ((x_end - x) + (y_end - y))
                    # print(x, x_end, y, y_end, s, p)
                    if s > ms:
                        ms = s
                        mp = p
                    elif s == ms and p < mp:
                        mp = p
print(f'{ms=}, {mp=}')
