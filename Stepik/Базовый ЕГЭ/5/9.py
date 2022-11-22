for i in range(1000):
    n = i - i % 4
    n = bin(n)[2:]
    n = n + str(n.count('1') % 2)
    n = n + str(n.count('1') % 2)
    r = int(n, 2)
    if r > 56:
        print(i, r)
