f = [1] * 2500
for n in range(4, 2100):
    f[n] = (2 * n) + f[n - 3]
print(f[2028] - f[2024])
