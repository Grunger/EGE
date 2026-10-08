for i in range(2000):
    s = i
    s = (s + 5) // 3
    n = 2
    while s > 0:
        s = s - n
        n = n * 2 + 1
    print(i, n)