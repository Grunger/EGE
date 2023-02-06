f = open('17_3.txt')
data = [int(i) for i in f]
k = len([i for i in data if i % 100 == 0])
ans = []
for a, b in zip(data, data[1:]):
    if (a < 0 or b < 0) and (a + b < k):
        ans.append(a + b)
print(len(ans), min(ans))
