def f(n):
    if n <= 0:
        print('!!!')
    if n == 1:
        return 2
    if n % 2 == 0:
        return (f(n - 1) + 2) // 3
    return 2 * f(n - 1) // f(n - 2) + 1



try:
    for i in range(1, 50):
        print(i, f(i))
except ZeroDivisionError:
    print('!!!', i)
