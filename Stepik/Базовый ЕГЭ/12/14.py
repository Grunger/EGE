def divs(x):
    d = set()
    for i in range(2, x):
        if x % i == 0:
            d.add(i)
    return d


for m in range(1000):
    s = '>' + '1' * 10 + '2' * 20
    s = s + '3' * m
    while '>1' in s or '>2' in s or '>3' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>3' in s:
            s = s.replace('>3', '1>', 1)
    s = s.replace('>', '')
    s = sum(int(i) for i in s)
    d = divs(s)
    if len(d) == 5:
        print(m, d)
        break
