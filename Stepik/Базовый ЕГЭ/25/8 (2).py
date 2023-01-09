from fnmatch import fnmatch


def divs(x):
    s = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            s.add(i)
            s.add(x // i)
            if i * x // i != x:
                return sorted(s)
    return sorted(s)

k = 0
for i in range(3674531, 369745931 + 1):
    if fnmatch(str(i), '36*745*31'):
        d = divs(i)
        if d:
            m = d[0] + d[-1]
            if m % 10 == 8:
                print(i, m)
                k += 1
                if k == 5:
                    break
