for i in range(1, 1000):
    n = i
    n = bin(n)[2:]
    if n[-1] == '0':
        n = '1' + n + '00'
    else:
        n = n + bin(n.count('1'))[2:]
    r = int(n, 2)
    if r > 219:
        print(i, r)
