from itertools import product
from random import randint


def slow():
    mx_k = 0
    mx_s = 0
    mask = list(product((0, 1), repeat=n))
    # print(mask)
    for item in mask:
        s = 0
        for i in range(n):
            if item[i] == 1:
                s += a[i]
        if s % 23 == 0:
            if s > mx_s:
                mx_s = s
                mx_k = sum(item)
            elif s == mx_s:
                mx_k = min(mx_k, sum(item))
    return mx_s, mx_k


def fast():
    s = sum(a)  # сумма всех чисел
    min_s = {i: 10**10 for i in range(23)}  # словарь с минимальными суммами
    min_k = {i: 0 for i in range(23)}  # соответствующее суммам количество чисел
    for x in a:  # перебираем все числа
        new_min_s = min_s.copy()  # делаем копию словаря
        new_min_k = min_k.copy()
        for i in range(23):  # перебираем все текущие минимальные суммы
            ost = (x + min_s[i]) % 23  # остаток от деления на 23 нового числа и текущей минимальной суммы
            # перезапоминаем минимальную сумму, если она меньше текущего минимального остатка
            # или равна ему, но при этом получена меньшим количеством чисел
            if x + min_s[i] < min_s[ost] or x + min_s[i] == min_s[ost] and 1 + min_k[i] > min_k[ost]:
                new_min_s[ost] = x + min_s[i]
                new_min_k[ost] = 1 + min_k[i]
        min_s = new_min_s
        min_k = new_min_k
        # проверяем, не является ли сам х минимальной суммой
        if x < min_s[x % 23]:
            min_s[x % 23] = x
            min_k[x % 23] = 1
    #     print(x, min_k)
    # print(s % 23)
    # print(s)
    # print(min_s)
    # print(min_k)
    if s % 23 == 0:
        return s, n
    return s - min_s[s % 23], n - min_k[s % 23]


f = open('27_B.txt')
n = int(f.readline())
a = [int(i) for i in f]
# print(slow())
print(fast())

# for i in range(100000):
#     n = 5
#     a = [randint(1, 100) for _ in range(n)]
#     if slow() != fast():
#         print('!!!')
#         print(slow(), fast())
#         print(a)
#         break
