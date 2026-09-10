def divs(x):
    s = set()
    for i in range(2, x):
        if x % i == 0:
            s.add(i)
    return sorted(s)


k = 0
for i in range(623457, 10 ** 9):
    d = divs(i)
    if d:
        m = d[0] + d[-1]
    if d and m % 13 == 5:
        print(i, m)
        k += 1
    if k == 5:
        break
