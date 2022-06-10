def minus(s, e):
    if s < e:
        return 0
    if s == e:
        return 1
    return minus(s - 2, e) + minus(s - 5, e)


print(minus(24, 3))
