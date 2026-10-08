d = dict()


def f_rec(s, e):
    if (s, e) in d:
        return d[(s, e)]
    if s in exclude:
        return 0
    if s > e:
        return 0
    if s == e:
        return 1
    a = 0
    for i in actions:
        a += f(eval(f'{s}{i}'), e)
    d[(s, e)] = a
    return a


def f(s, e):
    if s in exclude:
        return 0
    if s > e:
        return 0
    if s == e:
        return 1
    a = 0
    for i in actions:
        a += f(eval(f'{s}{i}'), e)
    return a


actions = ('+2', '+3', '*10+1')
exclude = []
print(f(3, 12) * f(12, 25))
