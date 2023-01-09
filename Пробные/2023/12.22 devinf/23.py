def f(st, fn):
    if st < fn:
        return 0
    if st == fn:
        return 1
    return f(st - 1, fn) + f(st // 2, fn)


print(f(89, 30) * f(30, 7))
