def f(n, e, s):
    if n > e:
        return 0
    if n == e:
        if s.count('2') + s.count('3') > s.count('1'):
            return 1
        return 0
    return f(n + 3, e, s + '1') + f(n * 2, e, s + '2') + f(n * 7, e, s + '3')


print(f(2, 472, ''))
