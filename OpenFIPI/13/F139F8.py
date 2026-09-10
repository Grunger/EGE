def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    d = a // 10 % 10
    e = a % 10
    if d < e:
        return f(a + 1, b) + f( a // 100 * 100 + e * 10 + d, b)
    return f(a + 1, b)

print(f(100, 143))
