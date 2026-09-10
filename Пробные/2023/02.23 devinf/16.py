f = [1] * 20000
for i in range(10000, 1, -1):
    if i > 3000:
        f[i] = 1
    elif i % 2 == 0:
        f[i] = f[i + 1] - i + 1
    else:
        f[i] = f[i + 2] - 2 * i + 2

print(2 * f[39] - 2 * f[34])
