'''На каждом 3-м километре кольцевой автодороги с двусторонним движением установлены контейнеры для мусора.
Длина кольцевой автодороги равна 3N километров. Нулевой километр и 3N-й километр автодороги находятся в одной точке.
Известно количество мусора, которое накапливается ежедневно в каждом из контейнеров.
Из каждого пункта мусор вывозит отдельный мусоровоз. Стоимость доставки мусора вычисляется как произведение
 количества мусора на расстояние от пункта до центра переработки.
 Центр переработки отходов расположен в одном из пунктов сбора мусора таким образом, что общая стоимость
  доставки мусора из всех пунктов минимальна.

Определите минимальную суммарную стоимость доставки мусора из всех пунктов сбора в центр переработки отходов.'''


def fast():
    dist = n // 2
    minus = [0] * n
    minus[0] = sum(d[1:dist + 1])
    for i in range(1, n):
        minus[i] = minus[i - 1] + d[(i + dist) % n] - d[i]
    plus = [0] * n
    plus[0] = d[0] + sum(d[-(dist - 1):])
    for i in range(1, n):
        plus[i] = plus[i - 1] + d[i] - d[(i + dist) % n]
    cost = 0
    for j in range(dist + 1):
        cost += d[j % n] * j
        if j != dist:
            cost += d[- j] * j
    min_cost = cost
    for i in range(1, n):
        cost += plus[i - 1] - minus[i - 1]
        min_cost = min(min_cost, cost)
    return min_cost


def slow():
    min_cost = 10 ** 9
    dist = n // 2
    for i in range(n):
        cost = 0
        for j in range(dist + 1):
            cost += d[(i + j) % n] * j
            if j != dist:
                cost += d[i - j] * j
        min_cost = min(cost, min_cost)
    return min_cost


f = open('107_27_B.txt')
n = int(f.readline())
d = [int(i) for i in f]
# print(slow() * 3)
print(fast() * 3)
# 471228
# 49113954961677
