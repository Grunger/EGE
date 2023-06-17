for n in range(1, 100):
    s = '1' + '7' * n
    while '17' in s or '377' in s or '777' in s:
        s = s.replace('17', '1', 1)
        s = s.replace('377', '73', 1)
        s = s.replace('777', '3', 1)
    print(n, s.count('3'))
    if s.count('3') == 2:
        print(n)
        break
