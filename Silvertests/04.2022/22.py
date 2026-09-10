for i in range(1000):
    s = i
    P = 12
    Q = 5
    K1 = 0
    K2 = 0
    while s <= 85:
        s = s + P
        K1 = K1 + 1
    while s >= Q:
        s = s - Q
        K2 = K2 + 1
    K1 += s
    K2 += s
    if K1 == 5 and K2 == 21:
        print(i, K1, K2)
