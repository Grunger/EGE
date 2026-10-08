from random import randint


def slow(n, data):
    mn = 10 ** 9
    for i in range(n // 2):
        j = i + n // 2
        st = 0
        for k in range(n):
            dist_a = min(abs(k - i), abs(i + n - k), abs(k + n - i))
            dist_b = min(abs(k - j), abs(j + n - k), abs(k + n - j))
            if dist_a < dist_b:
                st += dist_a * data[k]
            else:
                st += dist_b * data[k]
            # print(k, st, dist_a, dist_b)
        # print(i, j, st)
        mn = min(mn, st)
    return mn


def fast(n, data):
    dist = (n - 2) // 4

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
        # print(plus[i - 1], data[i], data[(i + dist) % n] * dist, - data[i - dist], - data[(i + dist) % n] * dist)
        plus[i] = plus[i - 1] + data[i] + data[(i + dist + 1) % n] * dist - data[i - dist] - data[(i + dist) % n] * dist

    cost = [0] * n
    for i in range(dist + 1):
        cost[0] += i * data[i]
        cost[0] += i * data[-i]
        # print(k, st, dist_a, dist_b)
    for i in range(1, n):
        cost[i] = cost[i - 1] + plus[i - 1] - minus[i - 1]

    min_cost = cost[0] + cost[n // 2]
    for i in range(1, n // 2):
        min_cost = min(min_cost, cost[i] + cost[n // 2 + i])
    return min_cost


n = 8
for _ in range(10000):
    data = [randint(1, 10) for _ in range(n)]
    if fast(n, data) != slow(n, data):
        print(data, fast(n, data), slow(n, data))
        break
