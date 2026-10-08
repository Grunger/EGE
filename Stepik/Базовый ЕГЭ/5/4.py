for i in range(1000):
    n = bin(i)[2:]
    n = n + str(n.count('1') % 2)
    n = n + str(n.count('1') % 2)
    if int(n, 2) > 51:
        print(int(n, 2))

