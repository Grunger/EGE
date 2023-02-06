for n in range(2, 100, 2):
    s = '2' * (n // 2) + '1' * (n // 2)
    while '12' in s or '21' in s:
        if '12' in s:
            s = s.replace('12', '21', 1)
        else:
            s = s.replace('21', '111', 1)
    if len(s) > 100:
        print(n)
        break

