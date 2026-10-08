for i in range(1000):
    n = bin(i)[2:]
    if n[-1] == '1':
        n = '1' + n + '0'
    else:
        n = '1' + n + '1'
    if int(n, 2) < 96:
        print(int(n, 2))
        
