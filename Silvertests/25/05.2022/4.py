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
x = 600_001
while k < 5:
    d = divs(x)
    for i in d:
        if i > 89 and i // 10 % 10 == 9:
            print(x, i)
            k += 1
            break

    x += 1
