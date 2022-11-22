for i in range(1000):
    n = bin(i)[2:]
    if n.count('1') > n.count('0'):
        n = n + '1'
    else:
        n = n + '0'
    r = int(n, 2)
    if r < 98:
        print(i, r)
        
