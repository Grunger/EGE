from fnmatch import fnmatch


def divs(x):
    s = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            s.add(i)
            s.add(x // i)
    return sorted(s)


for i in range(23000000, 24000000):
    if fnmatch(str(i), '23?45?12'):
        d = divs(i)
        if len(d) == 6:
            print(i, sum(d))
