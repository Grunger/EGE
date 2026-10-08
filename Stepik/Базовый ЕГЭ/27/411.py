"""На каждом километре автомагистрали, начиная с первого, расположены пункты питания.
 Известна суточная потребность каждого пункта питания в количестве готовых обедов.
 По правилам готовую еду нельзя перевозить на расстояние, превышающее М км.

Для транспортировки используются термоконтейнеры вместимостью не более 4 готовых обедов.
Каждый термоконтейнер используется для доставки только в один пункт питания, при этом в каждый пункт питания
 может быть доставлено не более одного термоконтейнера с неполной загрузкой.
Компания-производитель расположила в двух пунктах питания два цеха для производства готовых обедов так,
что из этих цехов в пункты питания ежедневно отправляется максимальное количество термоконтейнеров с готовыми обедами.
Определите необходимое суммарное количество термоконтейнеров для
ежедневной перевозки готовых обедов в пункты питания из двух цехов."""
from math import ceil
from random import randint


def slow(n, m, d):
    max_k = 0
    for p1 in range(m, n - 2 * m):
        for p2 in range(p1 + 2 * m + 1, n - m):
            k = 0
            for i in range(p1 - m, p1 + m + 1):
                k += d[i]
            for i in range(p2 - m, p2 + m + 1):
                k += d[i]
            max_k = max(max_k, k)
    return max_k


def fast(n, m, d):
    k_all = []
    # считаем первый пункт на расстоянии m от начала
    k = 0
    for i in range(2 * m + 1):
        k += d[i]
    k_all.append(k)
    # считаем все остальные пункты
    for i in range(2 * m + 1, n):
        k -= d[i - 2 * m - 1]
        k += d[i]
        k_all.append(k)
    max_k = 0
    first_max = k_all[0]
    #print(k_all)
    #print(m, len(k_all))
    for i in range(2 * m + 1, len(k_all)):
        #print(i, k_all[i], end=" ")
        first_max = max(first_max, k_all[i - 2 * m - 1])
        max_k = max(max_k, first_max + k_all[i])
        #print(first_max, max_k)
    return max_k


def check():
    n = 15
    m = randint(1, 3)
    d = [randint(1, 10) for _ in range(n)]
    if slow(n, m, d) != fast(n, m, d):
        print(n, m)
        print(*d, sep=' ')
        print(slow(n, m, d), fast(n, m, d))


# for i in range(10000):
#     check()
f = open('411_27_B.txt')
n, m = map(int, f.readline().split())
d = [ceil(int(i) / 4) for i in f]
# print(slow(n, m, d))
print(fast(n, m, d))
# 17286
# 213947
