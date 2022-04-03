def f(n):
    if n <= 2:
        return 1
    if n % 2 == 1:
        return f(n - 1) - n
    return f(n - 2) - f(n - 1) + 2


for i in range(28):
    print(i, f(i))
