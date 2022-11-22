for n in range(1, 1000):
    s = '>' + '1' * 23 + '2' * n + '3' * 15
    while '>1' in s or '>2' in s or '>3' in s:
        if '>1' in s:
            s = s.replace('>1', '2>', 1)
        if '>2' in s:
            s = s.replace('>2', '21>', 1)
        if '>3' in s:
            s = s.replace('>3', '11>', 1)
    s = sum(int(i) for i in s[:-2])
    if s <= 147:
        print(n, s)

