def tr(x):
    return 10 <= abs(x) <= 99

data = [int(i) for i in open('1F0F94.txt')]
mx = max(i for i in data if abs(i) % 100 == 33)
ans = []
for a, b, c in zip(data, data[1:], data[2:]):
    if tr(a) + tr(b) + tr(c) == 2:
        if (a + b + c)**2 < mx:
            ans.append(a + b + c)
print(len(ans), max(ans))
