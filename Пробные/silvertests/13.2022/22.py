for x in range(1001, 10000, 2):
    L = x
    M = 428
    if L % 2 == 0:
        M = -1
    while L != M:
        if L > M:
            L = L - M
        else:
            M = M - L
    if 100 <= L <= 999:
        print(x)
