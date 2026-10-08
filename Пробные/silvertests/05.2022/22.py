for i in range(1000):
    s = i
    k1 = 0
    k2 = 0
    while s > 0:
        d = s % 6
        s = s - 6
        if (d % 2 == 0):
            k1 += 1
        else:
            k2 += 1
    print(i, k1 + k2)
