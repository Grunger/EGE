f_ = dict()
g_ = dict()


def f(n):
    if n in f_:
        return f_[n]
    if n <= 2:
        f_[n] = 1
        return 1
    if n % 2 != 0:
        f_[n] = f(n - 1) - n
        return f(n - 1) - n
    f_[n] = f(n - 2) + g(n - 1) + 2
    return f(n - 2) + g(n - 1) + 2


def g(n):
    if n <= 0:
        return 2
    if n % 2 != 0:
        return f(n - 1) - 2 * g(n - 2)
    return 2 * f(n - 2) - 2 * g(n - 1)


for x in range(100):
    print(x, f(x))
