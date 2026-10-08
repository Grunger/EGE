for s in range(64, 1000):
    n = 1
    s_old = s
    while n * s < 4096:
        s //= 2
        n *= 4
    if n == 1024:
        print(s_old, n)
