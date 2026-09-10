for s in range(10000):
    s_ = s
    s = s // 10
    n = s
    while s < 125:
        s = s + 5
        n = n - 13
    if n == 0:
        print(s_)

