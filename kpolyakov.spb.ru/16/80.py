def f(n):
    if n <= 5:
        return 5
    if n % 3 == 0:
        return n + f(n // 3 + 2)
    return n + f(n + 3)


s = [-1] * 1000
for n in range(1000 - 3):
    if n <= 5:
        s[n] = 5
    elif n % 3 == 0 and s[n // 3 + 2] != -1:
        s[n] = n + s[n // 3 + 2]
    elif n % 3 != 0 and s[n + 3] != -1:
        s[n] = n + f[n + 3]
for i in range(1000):
    if s[i] != -1:
        print(i, s[i])
