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
x = 850_001
while k < 5:
    d = divs(x)
    count = []
    for i in d[::-1]:
        i = str(i)
        if len(i) > 2 and any(f'5{j}1' in i for j in range(10)):
            count.append(i)
    if count and len(count) % 5 == 0:
        print(x, max(count))
        k += 1
    x += 1
