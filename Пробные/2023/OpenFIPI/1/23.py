s = [0] * 100
s[4] = 1
for i in range(4, 11):
    s[i + 1] += s[i]
    s[i + 2] += s[i]
    s[i * 3] += s[i]
for i in range(11, 100):
    s[i] = 0
for i in range(10, 23):
    if i != 20:
        s[i + 1] += s[i]
        s[i + 2] += s[i]
        s[i * 3] += s[i]
print(s[22])


def f(st, fn):
    if st > fn or st == 20: return 0
    if st == fn: return 1
    return f(st + 1, fn) + f(st + 2, fn) + f(st * 3, fn)


print(f(4, 10) * f(10, 22))
