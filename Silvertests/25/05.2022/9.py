def is_simple(x):
    d = divs(x)
    return len(d) == 0


def all_divs(x):
    d = set()
    k = 1
    while k ** 2 <= x:
        if x % k == 0:
            d.add(k)
            d.add(x // k)
        k += 1
    return sorted(d)


def divs(x):
    d = set()
    k = 2
    while k ** 2 <= x:
        if x % k == 0:
            d.add(k)
            d.add(x // k)
        k += 1
    return sorted(d)


m = 0
for x in range(210000, 220000 + 1):
    d = all_divs(x)
    d = [i for i in d if '00' in str(i)]
    m = max(m, len(d))
print(m)
for x in range(210000, 220000 + 1):
    d = divs(x)
    if len(d) == m:
        print(x, max(d))
