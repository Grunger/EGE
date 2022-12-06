from random import randint


def slow(data, n, m):
    capacity = 6
    data_k = [i // capacity + bool(i % capacity) for i in data]
    data_mx = [0] * n
    mx = 0
    for i in range(2 * m + 1):
        mx += data_k[i]
    data_mx[m] = mx
    for i in range(m + 1, n - m):
        mx -= data_k[i - m - 1]
        mx += data_k[i + m]
        data_mx[i] = mx
    for first in range(m, n - 3 * m - 1):
        for second in range(first + 2 * m + 1, n - m):
            # 3750000
            if first % 100000 == 0:
                print(first, second, data_mx[first] + data_mx[second], mx)
            mx = max(mx, data_mx[first] + data_mx[second])
    return mx


def fast(data, n, m):
    capacity = 6
    data_k = [i // capacity + bool(i % capacity) for i in data]
    data_mx = [0] * n
    mx = 0
    for i in range(2 * m + 1):
        mx += data_k[i]
    data_mx[m] = mx
    for i in range(m + 1, n - m):
        mx -= data_k[i - m - 1]
        mx += data_k[i + m]
        data_mx[i] = mx
    first_mx = data_mx[m]
    mx = 0
    for i in range(3 * m + 1, n - m):
        if data_mx[i] + first_mx > mx:
            mx = data_mx[i] + first_mx
        first_mx = max(first_mx, data_mx[i - 2 * m])
    return mx


for _ in range(1000):
    n = randint(10, 15)
    m = randint(1, 2)
    d = [randint(1, 15) for _ in range(n)]
    if slow(d, n, m) != fast(d, n, m):
        print(d, n, m)
        print(slow(d, n, m))
        print(fast(d, n, m))
        break
