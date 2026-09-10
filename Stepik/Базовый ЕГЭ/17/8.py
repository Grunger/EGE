f = open('17_1.txt')
data = [int(i) for i in f]
k = max([i for i in data if i % 10 == 2])
ans = []
for a, b in zip(data, data[1:]):
    if a % 2 != 0 and b % 2 != 0 and a + b >= k:
        ans.append(a + b)
print(len(ans), max(ans))
