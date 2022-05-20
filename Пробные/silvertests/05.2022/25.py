def divs(x):
    s = set()
    k = 1
    while k ** 2 <= x:
        if x % k == 0:
            s.add(k)
            s.add(x // k)
        k += 1
    return s


k = 0
for n in range(400_000, 4068_00):
    d = sum(divs(n))
    s = str(d)
    if s[0] == '4' and s[-1] == '0' and '9' in s and d % 23 == 0:
        print(n, d // 23)
