def f(s, n):
    if s == 220 or s < n:
        return 0
    if s == n:
        return 1

    return f(s - 5, n) + f(s // 5, n)


for i in range(5, 251):
    print(i, f(i, 5))
