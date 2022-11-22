for i in range(1, 1000):
    n = i
    n = bin(n)[2:]
    if n.count('1') % 2 == 0:
        n = n + '0'
        n = '10' + n[2:]
    else:
        n = n + '1'
        n = '11' + n[2:]
    r = int(n, 2)
    if r >= 66:
        print(i, r)
