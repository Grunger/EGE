for i in range(10):
    n = 6**i
    k = 0
    while n > 1:
        k = k + 1
        if n % 6 == 0:
            n = n // 6
    print(i, end=' ')
    if k < 4:
        print(k)
    else:
        print(k % 4)