for i in range(1000):
    n = bin(i)[2:]
    n += str(n.count('1') % 2)
    n += str(n.count('1') % 2)
    r = int(n, 2)
    if r > 452:
        print(i, r)
