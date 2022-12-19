import math
from itertools import accumulate
from random import randint


def slow(n, capacity, a):
    data = dict()
    for i in range(n):
        p, k = a[i]
        data[p] = math.ceil(k / capacity)
    last = max(data)
    min_cost = 10 ** 10
    for p1 in range(last + 1):
        cost = 0
        for i in range(last + 1):
            cost += abs(p1 - i) * data.get(i, 0)
        min_cost = min(cost, min_cost)
    return min_cost


def fast(n, capacity, a):
    data = dict()
    for i in range(n):
        p, k = a[i]
        data[p] = math.ceil(k / capacity)
    last = max(data)
    for i in range(last):
        if i not in data:
            data[i] = 0
    data = {i: data[i] for i in sorted(data)}
    pref = [0] * 10 ** 8
    post = [0] * 10 ** 8
    for i, k in enumerate(accumulate(data.values())):
        post[i] = k
    data1 = {i: data[i] for i in list(data)[::-1]}
    for i, k in enumerate(list(accumulate(data1.values()))[::-1]):
        pref[i] = k
    pref.pop(0)
    cost = 0
    for i in range(last + 1):
        cost += (i - 1) * data[i]
    min_cost = cost
    for i in range(1, last + 1):
        cost += post[i] - pref[i]
        min_cost = min(min_cost, cost)
    return min_cost


for i in range(100):
    n = 20
    a = [[1, 10]]
    for _ in range(n):
        a.append([randint(max(b[0] for b in a), max(b[0] for b in a) + randint(2, 10)), randint(1, 100)])
    capacity = randint(10, 50)
    s = slow(n, capacity, a)
    f = fast(n, capacity, a)
    if s != f:
        print(capacity)
        print(a)
        break
    else:
        print(i, 'Good', s, f, a)
else:
    print('All OK')