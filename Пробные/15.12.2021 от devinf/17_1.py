f = list(map(int, open('17.txt').readlines()))
k = 0
m = 30000
for i in range(len(f) - 1):
	if f[i] % 3 == 0 and f[i + 1] % 3 == 0 and f[i] % 5 != 0 and f[i + 1] % 5 != 0:
		k += 1
		if f[i] + f[i + 1] > 0:
			m = min(m, f[i] + f[i + 1])
print(k, m) 
	
