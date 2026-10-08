f = open('27-T.txt')
n = int(f.readline())
data = [int(i) for i in f]
mn = 10 ** 9
# индекс первого пункта сбора мусора
for i in range(n // 2):
    # индекс второго пункта сбора мусора
    j = i + n // 2
    # стоимость текущего варианта расположения
    st = 0
    # перебираем все контейнеры
    for k in range(n):
        # вычисляем расстояние до ближайшего пункта сбора мусора
        # либо по часовой стрелке, либо против
        dist_a = min(abs(k - i), abs(i + n - k))
        dist_b = min(abs(k - j), abs(j + n - k))
        # добавляем к стоимости перевозку туда, куда ближе
        if dist_a < dist_b:
            st += dist_a * data[k]
        else:
            st += dist_b * data[k]
        # print(k, st, dist_a, dist_b)
    # print(i, j, st)
    mn = min(mn, st)
print(mn)
# 69572

