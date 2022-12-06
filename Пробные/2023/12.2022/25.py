from fnmatch import fnmatch


def divs(x):
    d = set()
    k = 2
    while k ** 2 <= x:
        if x % k == 0:
            d.add(k)
            d.add(x // k)
        k += 1
    return sorted(d)


i = 1
while i <= 10 ** 7:
    n = i
    if fnmatch(str(n), '3*52?'):
        d = divs(n)
        if len(d) % 2 == 1:
            print(n, d[-1])
    i += 1


# 3143529 1047843
# 3175524 1587762
# 3200521 1789
# 3845521 103933
# 3908529 1302843