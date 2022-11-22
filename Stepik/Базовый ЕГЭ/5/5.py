for i in range(1000):
    n = bin(i)[2:]
    if n[-1] == '1':
        n = n + '01'
    else:
        n = n + '10'
    if int(n, 2) > 84:
        print(int(n, 2))
        
