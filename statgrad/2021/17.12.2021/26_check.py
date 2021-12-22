from random import randint


def fast(a):
    d = dict()
    # Словарь хранит изменение количества запущенных
    # процессов по участвующим моментам времени
    for x in a:
        if x[0] < start:
            x[0] = start - 1
        if x[1] == 0 or x[1] > end:
            x[1] = end + 1
        d[x[0]] = d.get(x[0], 0) + 1
        d[x[1]] = d.get(x[1], 0) - 1
    # Для известных участков считаем количество запущенных процессов
    run = 0
    d2 = sorted(d.keys())
    m = -n
    for i in d2:
        run += d[i]
        if start <= i <= end:
            if run >= m:
                m = run
    # Считаем расстояние между точками где количество
    # процессов равно максимальному
    run = 0
    k = 0
    for i in d2:
        run += d[i]
        if start <= i <= end:
            if run == m:
                k += d2[d2.index(i) + 1] - i
    return m, k


def slow(a):
    d = dict()
    for i in a:
        for j in range(i[0], i[1] + 1):
            d[j] = d.get(j, 0) + 1
    m = 0
    for i in range(start, end + 1):
        m = max(m, d[i])
    k = 0
    for i in range(start, end + 1):
        if d[i] == m:
            k += 1
    return m, k


for i in range(100):
    n = 50
    a = []
    while len(a) < n:
        s = 1633046400
        f = 1633046400 + 30 * 24 * 60 * 60
        st = randint(s, f)
        fn = randint(s, f)
        if randint(0, 100) < 5:
            st = 0
        if randint(0, 100) < 5:
            fn = 0
        if fn > st or fn == 0:
            a.append([st, fn])
    start = 1633305600
    end = 1633305600 + 7 * 24 * 60 * 60  # 1633910400
    if fast(a) == slow(a):
        print('ok')
    else:
        print('bad')
