def f(st, fn, k):
    if st > fn or k > 3:
        return 0
    if st % 2 == 0:
        f(st + 1, fn, k + 1)
        f(st + 2, fn, k + 1)
        f(st * 3, fn, k + 1)
        ans.append(st)
        return 1
    return f(st + 1, fn, k + 1) + f(st + 2, fn, k + 1) + f(st * 3, fn, k + 1)


ans = []
f(4, 4 * 3 ** 3, 0)
print(sorted(ans))
print(len(ans))
