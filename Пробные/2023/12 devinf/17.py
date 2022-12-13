f = open('17.txt').read().strip().split()
data = [int(i) for i in f]
mx10 = min([i for i in data if i % 123 == 0])
ans = []
for a, b in zip(data, data[1:]):
	if (a % 2023 >= mx10) != (b % 2023 >= mx10):
		ans.append(a + b)
print(ans)
print(mx10)
print(len(ans), max(ans))
