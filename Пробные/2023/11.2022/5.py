for i in range(4, 100):
    n = bin(i)[2:]
    if n.count('1') % 2 == 0:
        n = n + '1'
        n = '10' + n[2:]
    else:
        n = n + '11'
        n = '1' + n[2:]
    if int(n, 2) >= 100:
        print(i)
        break
