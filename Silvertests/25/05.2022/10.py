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
    d = divs(x)
    new_d = []
    for i in d:
        if all(f'0{c}{d}3' not in str(i) for c in range(10) for d in range(10)):
            new_d.append(i)
    #d = [i for i in d for c in range(10) if f'0{c}0' not in str(i)]
    m = max(m, len(new_d))
# print(m)
for x in range(210000, 220000 + 1):
    d = divs(x)
    if len(d) == m:
        print(x, max(d))
