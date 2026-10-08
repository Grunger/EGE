def f(a, b):
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a + 1, b) + f(a * 2, b)


print(f(2, 31) * f(31, 43) * f(43, 86))
