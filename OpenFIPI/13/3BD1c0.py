def f(st, fn):
    if st > fn:
        return 0
    if st == fn:
        return 1
    return f(st + 1, fn) + f(st + 4, fn)


print(f(3, 15))
