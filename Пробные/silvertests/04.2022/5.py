for i in range(1, 1000):
    n = bin(i)[2:]
    if i % 2 == 0:
        n = n + '11'
    else:
        n = '1' + n + '10'
    n = int(n, 2)
    if n > 632:
        print(i)
        break