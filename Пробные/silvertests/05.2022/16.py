def f(n):
    if n <= 2:
        return 1
    if n % 3 != 0:
        return f(n - 1) - f(n - 2) + n
    return 4 * f(n - 1) - 2 * f(n - 2) -  3 * n


print(f(31))
