def is_simple(x):
    d = divs(x)
    return len(d) == 0

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
x = 970_001
while k < 5:
    d = divs(x)
    count = []
    for i in d:
        if is_simple(i) and '3' in str(i):
            count.append(i)
    if len(count) > 3:
        k += 1
        print(x, max(count))
    x += 1
