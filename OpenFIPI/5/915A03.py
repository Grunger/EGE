for i in range(100, 1000):
    N = i
    a = (N // 100) * ((N // 10) % 10)
    b = (N // 10 % 10) * (N % 10)
    R = int(str(min(a, b)) + str(max(a, b)))
    if R == 621:
        print(N)
        break
