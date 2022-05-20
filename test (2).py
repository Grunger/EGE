def f(st, fn, way):
    if way.count('3') > 1:
        return 0
    if st > fn:
        return 0
    if st == fn:
        if '3' in way:
            return 1
        else:
            return 0
    return f(st + 1, fn, way + '1') + \
           f(st + 2, fn, way + '2') + \
           f(st * 2, fn, way + '3')


print(f(2, 12, ''))
