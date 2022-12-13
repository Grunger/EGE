for i in range(1, 15):
    n = bin(i)[2:]
    if n.count('1') % 2 == 0:
        n = n + '1'
        n = '10' + n[2:]
    else:
        n = n + '0'
        n = '11' + n[2:]
    print(i, int(n, 2))
