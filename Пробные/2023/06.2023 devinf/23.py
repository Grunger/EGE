def f(st, fn):
    if st > fn or st == 13:
        return 0
    if st == fn:
        return 1
    return f(st + 1, fn) + f(st * 2, fn) + f(st * 3, fn)


print(f(3, 8) * f(8, 18))
