for i in range(1, 1000):
    n = i
    s = ''
    while n:
        s = str(n % 5) + s
        n //= 5
    if int(s[-1]) % 2 == 0:
        s = s + '2'
    else:
        s = '2' + s + '3'
    s = int(s, 5)
    if s < 1000:
        print(i, s)
