def f(st, fn):
    if st == 17:
        return 0
    if st > fn:
        return 0
    if st == fn:
        return 1
    return f(st + 1, fn) + f(st * 2, fn) + f(st ** 2, fn)


print(f(2, 16) * f(16, 65))
