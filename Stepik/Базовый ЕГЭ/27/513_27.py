from random import randint
from math import ceil

CAPACITY = 45


def slow():
    count = 10000000
    data = [0] * count
    for line in f:
        i, j = map(int, line.split())
        data[i - 1] = j
    mx = 0
    for i in range(count):
        k = 0
        if data[i] == 0:
            continue
        k += data[i] // CAPACITY + bool(data[i] % CAPACITY)
        for j in range(i - 1, i - m - 1, -1):
            if j >= 0:
                k += data[j] // CAPACITY + bool(data[j] % CAPACITY)
        for j in range(i + 1, i + m + 1):
            if j < count:
                k += data[j] // CAPACITY + bool(data[j] % CAPACITY)
        # print(i + 1, k)
        mx = max(mx, k)
    return mx


def fast():
    points = dict()
    w = [0] * 10 ** 8
    for i in range(n):
        num, k = map(int, f[i].split())
        points[num] = k
        w[num] = k // CAPACITY + bool(k % CAPACITY)
    start = min(points)
    k = 0
    for i in range(start, start - m, -1):
        if i < 0:
            break
        k += w[i]
    for i in range(start + 1, start + m + 1):
        k += w[i]
    mx = k
    for i in range(start + 1, max(points) + 1):
        k -= w[i - m - 1]
        k += w[i + m]
        # print(i, k)
        if i not in points:
            continue
        # print(i, k)
        mx = max(k, mx)
    return mx


def check():
    for _ in range(1000):
        print(_)
        n, m = randint(5, 10), randint(3, 5)
        p = set()
        f = []
        while len(f) < n:
            point = randint(1, 50)
            if point not in p:
                f.append(f'{point} {randint(1, 200)}')
                p.add(point)
        a, b = slow(), fast()
        if a != b:
            print(n, m)
            print(sorted([[int(j) for j in i.split()] for i in f]))
            print(a, b)
            break


f = open('513_27_B.txt')
n, m = map(int, f.readline().split())
f = f.read().strip().split('\n')
# print(slow())
print(fast())

# 295
# 98086
