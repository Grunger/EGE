for i in range(100):
    n = oct(i)[2:]
    if i % 2 == 0:
        n = n + '57'
    else:
        n = '5' + n + '2'
    n = int(n, 8)
    if n < 1000:
        print(i)

