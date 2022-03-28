def f(s_old, s, e):
    if s in exclude:
        return 0
    if s > e:
        return 0
    if s == e:
        return 1
    if s - s_old == 1:
        return f(s, s + 3, e) + f(s, s ** 2, e)
    if s - s_old == 3:
        return f(s, s + 1, e) + f(s, s ** 2, e)
    if s_old == 0:
        return f(s, s + 1, e) + f(s, s + 3, e) + f(s, s ** 2, e)
    return f(s, s + 1, e) + f(s, s + 3, e)


exclude = [6]
print(f(0, 2, 5) * f(0, 5, 33))

# +1 +3 **2