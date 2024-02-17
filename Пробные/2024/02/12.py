for n in range(4, 10000):
    s = '5' + '2' * n
    while '52' in s or '2222' in s or '1122' in s:
        s = s.replace('52', '111', 1)
        s = s.replace('2222', '5', 1)
        s = s.replace('1122', '25', 1)
    if sum(int(i) for i in s) == 2024:
        print(n)
