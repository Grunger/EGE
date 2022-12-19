data = [int(i) for i in open('17.txt').read().split()]
mx10 = max(i for i in data if i % 100 == 10)
ans = []
for a, b in zip(data, data[1:]):
    if (a % 2023) * (b % 2023) >= mx10:
        ans.append(a + b)
print(len(ans), min(ans))
