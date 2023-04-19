from itertools import accumulate
from math import ceil
from random import randint


def slow(n, m, f):
    d = dict()
    for s in f:
        p, c = map(int, s.split())
        d[p] = ceil(c / m)
    min_cost = 10 ** 9
    for p1 in range(max(d)):
        cost = 0
        for p in d:
            cost += abs(p - p1) * d[p]
        min_cost = min(min_cost, cost)
    return min_cost

def fast(n, capacity, f):
    data = dict()
    for i in range(n):
        p, k = map(int, f[i].split())
        data[p] = ceil(k / capacity)
    last = max(data)
    for i in range(last):
        if i not in data:
            data[i] = 0
    data = {i: data[i] for i in sorted(data)}

    pref = [0] * (last * 2 + 1)
    post = [0] * (last * 2 + 1)
    for i, k in enumerate(accumulate(data.values())):
        post[i] = k
    data1 = {i: data[i] for i in list(data)[::-1]}
    for i, k in enumerate(list(accumulate(data1.values()))[::-1]):
        pref[i] = k
    pref.pop(0)
    # print(pref)
    # print(post)
    cost = 0
    for i in range(last + 1):
        cost += (i - 1) * data[i]
    min_cost = cost
    for i in range(1, last + 1):
        cost += post[i] - pref[i]
        min_cost = min(min_cost, cost)
    return min_cost


def sn(n, m, f):
    a = [list(map(int, s.split())) for s in f]  # взяли парами из файла
    x = a[n - 1][0]  # фиксируем самую большую координату
    b = [0] * (x + 1)  # создаем сплошной массив на всю длину
    for i in range(n):
        b[a[i][0]] = (a[i][1] + m - 1) // m  # фиксируем в массиве данные о количестве отправлений на известных пунктах
    min_cost = 10 ** 22  # задаем бесконечность как ответ
    n = x + 1  # размер исследуемой прямой меняем на x + 1
    st = sum([i * b[i] for i in range(n)])  # склад в 0 отметке - стоимость перевозок до каждого i-го пункта равна i
    pref = [0] * n  # префиксные суммы
    post = [0] * n  # постфиксные суммы
    for i in range(n):  # для всех пунктов считаем префикс и постфикс
        post[n - i - 1] = post[(n - i) % n] + b[n - i - 1]
        pref[i] = pref[i - 1] + b[i]

    for i in range(1, n):  # переносим склад по всем точкам от 1 до x, находим минимальную стоимость
        st = st - post[i] + pref[i - 1]
        min_cost = min(st, min_cost)
    return min_cost

for _ in range(100):
    n = 6
    m = 5
    p = set()
    while len(p) < n:
        p.add(randint(1, 10))
    c = [randint(1, 10) for _ in range(n)]
    f = [f'{sorted(p)[i]} {c[i]}' for i in range(n)]
    if fast(n, m, f) != sn(n, m, f):
        print(f)
        print(fast(n, m, f), sn(n, m, f))
