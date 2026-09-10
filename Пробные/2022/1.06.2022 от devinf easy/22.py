for i in range(1000):
    x = i
    L = 0
    M = 0
    while x > 0:
        M = M + 1
        if x % 2 != 0:
            L = L + 1
        x = x // 2
    if L == 7 and M == 8:
        print(i, L, M)