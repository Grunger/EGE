def divs(x):
    d = set()
    k = 2
    while k * k <= x:
        if x % k == 0:
            d.add(k)
            d.add(x // k)
        k += 1
    return d


a = 750_001
k = 0
while k < 5:
    d = [i for i in divs(a) if i != 17 and i != a and i % 100 == 17]
    if d:
        print(a, max(d))
        k += 1
    a += 1