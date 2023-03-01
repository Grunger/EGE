f = open('27-B.txt')
n = int(f.readline())
data = [int(i) for i in f]

dist = n // 2 // 2
minus = [0] * n
for i in range(1, dist + 1):
    minus[0] += data[i]
minus[0] += data[-dist] * dist
for i in range(1, n):
    minus[i] = minus[i - 1] - data[i] - data[-dist + i - 1] * dist + data[(i + dist) % n] + data[-dist + i] * dist

plus = [0] * n
for i in range(0, -dist, -1):
    plus[0] += data[i]
plus[0] += data[dist + 1] * dist
for i in range(1, n):
    plus[i] = plus[i - 1] + data[i] + data[(i + dist + 1) % n] * dist - data[i - dist] - data[(i + dist) % n] * dist

# стоимость первого пункта
cost = [0] * n
for i in range(dist + 1):
    cost[0] += i * data[i]
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

# 26483479389268
