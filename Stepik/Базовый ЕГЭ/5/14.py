for i in range(1, 1000):
    n = i
    n = bin(n)[2:]
    if n[-1] == '0':
        n = '1' + n + '00'
    else:
        n = '11' + n + '11'
    r = int(n, 2)
    if r > 400:
        print(i, r)
