from itertools import permutations, product


def f(x, y, z, w):
    return not (w <= (x == y)) and (z <= x)


s = 'xyzw'
for p in permutations((0, 1, 2, 3)):
    p1, p2, p3, p4 = p
    for a1, a2, a3, a4, a5 in product((0, 1), repeat=5):
        t = [
            (a1, 0, 1, 0),
            (0, a2, a3, 0),
            (a4, 1, 1, a5)
        ]
        if len(set(t)) != 3:
            continue
        # fl = True
        # for st in t:
        #     if not f(st[p1], st[p2], st[p3], st[p4]):
        #         fl = False
        # if fl:
        #     print(p)
        if all(f(st[p1], st[p2], st[p3], st[p4]) for st in t):
            print(p)

# заполнение пяти пропусков таблицы, для этого перебираем все
# комбинации 0 и 1 длины равной количеству пропусков
for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    # на основании комбинаций значений а1…а5 строим таблицу из трёх строк
    table = [(a1, 0, 1, 0), (0, a2, a3, 0), (a4, 1, 1, a5)]
    # проверяем, что полученные строки таблицы различны, т.е. длина таблицы
    # равна длине списка
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            # проверка значений строк
            if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1]:
                print(p)
