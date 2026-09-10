for i in range(1000):
    n = bin(i)[2:]
    if n[-1] == '0':
        n = n + '00'
    else:
        n = '11' + n
    if int(n, 2) < 131:
        print(i)
        
