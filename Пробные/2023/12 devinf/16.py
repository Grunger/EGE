f = [1] * 2500
for n in range(3, 2100):
	if n % 2 == 0:
		f[n] = f[n - 3] + 2 * n
	else:
		f[n] = f[n - 1] + n
print(f[2048] - f[2041])

