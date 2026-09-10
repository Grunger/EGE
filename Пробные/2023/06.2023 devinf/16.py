f = [0] * 5000
for i in range(4000, 0, -1):
    if i > 3000:
        f[i] = i
    else:
        f[i] = f[i + 2] + 2
print(f[40] - f[43])
