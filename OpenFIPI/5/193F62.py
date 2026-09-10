for i in range(1, 1000):
    N = i
    p = bin(N)[2:]
    p = p + str(p.count('1') % 2)
    p = p + str(p.count('1') % 2)
    R = int(p, 2)
    if R > 89:
        print(i)
        break
