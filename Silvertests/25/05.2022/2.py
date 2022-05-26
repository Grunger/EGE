def divs(x):
    d = set()
    k = 2
    while k ** 2 <= x:
        if x % k == 0:
            d.add(k)
            d.add(x // k)
        k += 1
    return sorted(d)


def m(x):
    d = divs(x)
    if len(d) == 0:
        return 0
    return d[0] + d[-1]


k = 0
for i in range(1_200_001, 1_250_000):
    a = str(m(i))
    # print(i, a)
    # # if len(a) == 6 and a[0] == '3' and a[1] == '5' and a[4:] == '23':
    if a[1:3] == '09' and a[-1] == '1':
        print(i, m(i))
        k += 1
    if k > 4:
        break
