for x in range(200, 100, -1):
    B = x
    A = 9
    D = x
    S = 0
    while D // 2 > 0:
        if D % 2 == 1:
            S += 1
        else:
            S += A
        D = D // 2
    if S == 30:
        print(x)
