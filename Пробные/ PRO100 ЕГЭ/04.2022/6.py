for i in range(1, 10000):
    d = i
    n = 5
    s = 83
    while s <= 1200:
        s += d
        n += 6
    if n == 89:
        print(i)