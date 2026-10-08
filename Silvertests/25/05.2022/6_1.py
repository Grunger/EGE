from fnmatch import fnmatch


def divs(x):
    d = set()
    k = 2
    while k * k <= x:
        if x % k == 0:
            d.add(k)
            d.add(x // k)
        k += 1
    return d


k = 0
for i in range(850_000, 950_000):
    d = [j for j in divs(i) if fnmatch(str(j), '*5?1*')]
    if d and len(d) % 5 == 0:
        print(i, max(d))
        k += 1
    if k == 5:
        break

