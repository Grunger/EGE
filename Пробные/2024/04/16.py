f = [10] * 5000
for n in range(12, 4500):
    f[n] = n + f[n - 1]
print(f[4201] - f[4199])
