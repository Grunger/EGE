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


def f_len(s):
    return {s + 1, s + 3, s * 2, s * 3}


# actions = ('+1', '+3', '*2')
# exclude = [6]
# print(f(0, 2, 5), f(0, 5, 33))

n = {5}
k = 0
while any(i <= 150 for i in n):
    if 150 in n:
        k += 1
    n_new = set()
    while n:
        n_new = n_new.union(f_len(n.pop()))
    n = {i for i in n_new if i <= 150}
print(sorted(n))
print(k)
