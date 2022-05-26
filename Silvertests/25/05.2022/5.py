def divs(x):
    d = set()
    k = 2
    while k ** 2 <= x:
        if x % k == 0:
            d.add(k)
            d.add(x // k)
        k += 1
    return sorted(d)


k = 0
x = 700_001
while k < 5:
    d = divs(x)
    for i in d[::-1]:
        i = str(i)
        if len(i) == 3 and i[0] == '1' and i[-1] == '3':
            print(x, i)
            k += 1
            break
    x += 1
