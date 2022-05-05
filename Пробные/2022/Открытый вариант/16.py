def f(n):
    if n < 3:
        return 2
    if n % 2 == 0:
        return f(n - 2) + f(n - 1) - n
    return f(n - 1) - f(n - 2) + 2 * n

print(f(32))
