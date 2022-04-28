def f(n):
    if n <= 2:
        return 2
    if n % 2 != 0:
        return 2 * f(n - 1) + f(n - 2) - n
    return f(n - 1) - f(n - 2) + 2 * n


print(f(31))
