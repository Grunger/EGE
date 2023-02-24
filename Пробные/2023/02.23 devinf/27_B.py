f = open('27-B_old.txt')
n = int(f.readline())
data = [int(i) for i in f]
mn = 10 ** 9

dist = n // 2 // 2

minus = [0] * n
# для четных
# for i in range(1, dist + 1):
#     minus[0] += data[i]
# minus[0] += data[-dist] * dist
# for i in range(1, n):
#     minus[i] = minus[i - 1] - data[i] - data[-dist + i - 1] * dist + data[(i + dist) % n] + data[-dist + i] * dist

# для нечетных
for i in range(1, dist + 1):
    minus[0] += data[i]
minus[0] += data[-dist + 1] * (dist - 1)
for i in range(1, n):
    # динамичный подсчет минусов
    # новый минус это предыдущий минус текущая точка
    minus[i] = minus[i - 1] - data[i] - data[i - dist] * (dist - 1) + data[(i + dist) % n] + data[i - dist + 1] * (
                dist - 1)

# для четных
# plus = [0] * n
# for i in range(0, -dist, -1):
#     plus[0] += data[i]
# plus[0] += data[dist + 1] * dist
# for i in range(1, n):
#     # print(plus[i - 1], data[i], data[(i + dist) % n] * dist, - data[i - dist], - data[(i + dist) % n] * dist)
#     plus[i] = plus[i - 1] + data[i] + data[(i + dist + 1) % n] * dist - data[i - dist] - data[(i + dist) % n] * dist

# для нечетных
plus = [0] * n
for i in range(0, -dist + 1, -1):
    plus[0] += data[i]
plus[0] += data[dist + 1] * dist
for i in range(1, n):
    # print(plus[i - 1], data[i], data[(i + dist) % n] * dist, - data[i - dist], - data[(i + dist) % n] * dist)
    plus[i] = plus[i - 1] + data[i] + data[(i + dist + 1) % n] * dist - data[i - dist + 1] - data[(i + dist) % n] * dist

# стоимость первого пункта
cost = [0] * n
for i in range(dist + 1):
    cost[0] += i * data[i]
for i in range(dist):
    cost[0] += i * data[-i]
    # print(k, st, dist_a, dist_b)
# стоимость всех остальных
for i in range(1, n):
    cost[i] = cost[i - 1] + plus[i - 1] - minus[i - 1]

# print('m', minus)
# print('p', plus)
# print('c', cost)
min_cost = cost[0] + cost[n // 2]
for i in range(1, n // 2):
    min_cost = min(min_cost, cost[i] + cost[n // 2 + i])
print(min_cost)

# 25827273956644
# 25827372462664