def f(st, fn, way):
    if st > fn:
        return 0
    if st == fn:
        # количество четных в траектории
        if len(list(filter(lambda x: x % 2 == 0, way))) == 2:
            print(way)
            return 1
        return 0
    return f(st + 1, fn, way + [st + 1]) + \
           f(st + 3, fn, way + [st + 3]) + \
           f(st + 5, fn, way + [st + 5])


print(f(3, 10, [3]))
