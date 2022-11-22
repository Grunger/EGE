for i in range(1, 1000):
    n = i
    n = bin(n)[2:]
    if n[-1] == '0':
        n = '110' + n
    else:
        n = '1' + n + '01'
    r = int(n, 2)
    if r > 745:
        print(i, r)
