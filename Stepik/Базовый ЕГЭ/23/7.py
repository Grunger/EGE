def f(st, fn):
    if st < fn:
        return 0
    if st == fn:
        return 1
    return f(st - 2, fn) + f(st - 5, fn)


print(f(27, 2))
