def f(s, n):
    if s == n:
        return 1
    if s > n or sum(int(i) for i in str(s)) == n:
        return 0
    return f(s + 2, n) + f(s + sum(int(i) for i in str(s)), n)


print(f(3, 29) * f(29, 68))

