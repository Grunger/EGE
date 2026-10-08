for i in range(10000):
    s = i
    s = (s - 5) // 13
    n = 1
    while s > 0:
        s = s - 3
        n = n * 2 + 1
    print(i, n)