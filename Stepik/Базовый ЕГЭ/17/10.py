f = open('17_3.txt')
data = [int(i) for i in f]
k = min(i for i in data if i > 0 and i % 7 == 0)
ans = []
for a, b in zip(data, data[1:]):
    if (a % 7 == 0 or b % 7 == 0) and (a + b) % k == 0:
        ans.append(a + b)
print(len(ans), max(ans))
