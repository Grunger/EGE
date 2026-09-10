def f(n):
    if n in (1, 2):
        return 1
    if n % 2 == 0:
        return int(n * f(n - 1) / 2)
    return int(n * (f(n - 1) + f(n - 2)) / 3)


print(f(13))
