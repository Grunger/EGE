f = [0] * 34
for n in range(2, 34):
    if n % 2 != 0:
        f[n] = (n + 1) // 2 + f[n - 1]
    else:
        f[n] = 2 * f[n - 1] + 1
print(f[33])
