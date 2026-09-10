f = open('17_5.txt')
data = [int(i) for i in f]
mn = min(data)
ans = []
for a, b in zip(data, data[1:]):
    if (a % 11 + b % 11) == mn:
        ans.append(a + b)
print(len(ans), min(ans))
