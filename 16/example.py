a = [0]


def f(n):
    a[0] += 2 * n + 1
    if n > 1:
        a[0] += 3 * n - 8
        f(n - 1)
        f(n - 4)

f(50)
print(a)
