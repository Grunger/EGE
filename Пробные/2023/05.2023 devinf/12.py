for n in range(6, 10000):
    s = '1' + '3' * n
    while '12' in s or '233' in s or '3333' in s:
        if '12' in s:
            s = s.replace('12', '332', 1)
        if '233' in s:
            s = s.replace('233', '23', 1)
        if '3333' in s:
            s = s.replace('3333', '32', 1)
    sm = sum(int(i) for i in s)
    print(n, sm)
    if sm % 6 == 0:
        print(n)
        break
