for i in range(1000):
    n = bin(i)[2:]
    n = n + str(n.count('1') % 2)
    n = n + str(n.count('1') % 2)
    if int(n, 2) > 125:
        print(i)
        break
