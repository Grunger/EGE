f = [1] * 34
for i in range(3, 34):
    if i % 2 == 0:
        f[i] = f[i - 1] + i - 1
    else:
        f[i] = f[i - 2] + 2 * i - 2

print(f[33])
