def f(s, fn):
    if s > fn:
        return 0
    if s == fn:
        return 1
    return f(s + 2, fn) + f(s * 2, fn)


print(f(1, 22) * f(22, 74))