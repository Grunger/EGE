def f(st, ed):
    if st > ed:
        return 0
    if st == ed:
        return 1
    return f(st + 3, ed) + f(st + 4, ed) + f(st * 3, ed)


print(f(1, 7) * f(7, 30))
