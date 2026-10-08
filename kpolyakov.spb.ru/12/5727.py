for n in range(17, 1000):
    s = '1' * n + '2' * n + '3' * n
    while '21' in s or '31' in s or '32' in s:
        if '21' in s:
            s = s.replace('21', '12', 1)
        if '31' in s:
            s = s.replace('31', '13', 1)
        if '32' in s:
            s = s.replace('32', '23', 1)

    if s[49] == '2':
        print(n * 3)
        break
