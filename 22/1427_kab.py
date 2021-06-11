def f(x):
    a = 0
    b = 0
    while x > 0:
        a += 1
        if x % 2 != 0:
            b += 1
        x //= 2
    return a, b


k = 0
for n in range(1, 100000):
    print(f(n))
    if f(n) == (16, 14):
        k += 1
print(k)
