k = 0
for x in range(100000000):
    a = 0
    b = 0
    m = 0
    d = 2
    while x > 0:
        b += 1
        if x % 2 == d:
            a += 1
        else:
            if a > m:
                m = a
            a = 1
            d = x % 2
        x //= 2
    if a > m:
        m = a
    if b == 20 and m == 15:
        k += 1
    if b > 20:
        break
print(k)
