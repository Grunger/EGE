def divs(x):
    d = set()
    k = 1
    while k ** 2 <= x:
        if x % k == 0:
            d.add(k)
            d.add(x // k)
        k += 1
        if 3 in d or 5 in d:
            break
        if k == 29 and not all(j in d for j in (7, 13, 17, 23, 29)):
            break
    return d


count = 0
for i in range(1000000000, 2000000001):
    if i % 1000000 == 0:
        print(i)
    d = divs(i)
    if all(k in d for k in (7, 13, 17, 23, 29)) and all(k not in d for k in (3, 5)) and len([i for i in d if i % 2 == 1]) > 100:
        count += 1
print(count)
