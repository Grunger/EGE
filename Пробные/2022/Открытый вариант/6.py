for i in range(1000):
    s = i
    s = (s - 21) // 10
    n = 1
    while s > 0:
        n = n * 2
        s = s - n
    if n == 32:
        print(i)
        break
