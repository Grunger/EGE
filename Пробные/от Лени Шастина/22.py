for i in range(16666655, 100000000):
    n = i
    a = 0
    b = 0
    while n >= 0:
        d = n % 10
        if d == 8:
            a += 1
        if d == 0:
            b += 1
        n = n - 1
    s = a + b
    print(i, s)
    if s == 3333333:
        break