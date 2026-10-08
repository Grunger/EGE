f = open('27_C.txt')
n = int(f.readline())
k = 0
s = 0
a = list(map(int, f.readlines()))
for i in range(n):
	for j in range(i, n):
		sm = sum(i for i in a[i:j + 1] if i % 2 == 0)
		# print(i, j, sm, sm % 61, k, s)
		if sm % 16 == 0:
			if sm >= s:
				s = sm
				k = j - i + 1
print(k, s)
		
