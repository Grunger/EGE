def f(st, fn):
    if st > fn:
        return 0
    if st == fn:
        return 1
    return f(st + 1, fn) + f(st * 2, fn) + f(st * 3, fn)


k = 0
for a in range(2, 20, 2):
    k += f(a, 15)
print(k)
