for n in range(4, 100000):
    s = '5' + '2' * n
    while '52' in s or '222' in s or '1122' in s:
        s = s.replace('52', '11', 1)
        s = s.replace('222', '5', 1)
        s = s.replace('1122', '25', 1)
    if sum(int(i) for i in s) == 2024:
        print(n)
