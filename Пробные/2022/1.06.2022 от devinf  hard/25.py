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
x = 960001
while k < 5:
    d = divs(x)
    count = []
    for i in d:
        if is_simple(i) and len(str(i)) > 1 and str(i)[-2] == '3':
            count.append(i)
    if len(count) > 2:
        k += 1
        print(x, sum(count))
    x += 1
