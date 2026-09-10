def f(s, e):
    if s == e:
        return 1
    if s < e:
        return 0
    return f(s - 1, e) + f(s // 2, e)


start = int('110111', 2)
finish = int('110', 2)
print(f(start, finish))
