def f(st, fn, way):
    if '11' in way or '22' in way or '33' in way:
        return 0
    if st == 6:
        return 0
    if st > fn:
        return 0
    if st == fn:
        return 1
    return f(st + 1, fn, way + '1') + \
           f(st + 3, fn, way + '2') + \
           f(st ** 2, fn, way + '3')


print(f(2, 5, ''), f(5, 33, ''))
