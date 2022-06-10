def f(s, way):
    if way > 6:
        return 0
    if way == 6:
        a.append(s)
    return f(s + 1, way + 1) + f(s * 2, way + 1)


a = []
f(2, 1)
print(sorted(a))
print(len(a) - len(set(a)))
