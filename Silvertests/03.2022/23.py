def f1(n):
    if n == 28:
        return 1
    if n < 28:
        return 0
    return f1(n - 2) + f1(n - 5)


def f2(n):
    if n == 5:
        return 1
    if n < 5:
        return 0
    return f2(n - 2) + f2(n - 5)


print(f1(48) *  f2(28))
