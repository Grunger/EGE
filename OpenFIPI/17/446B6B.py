def tr(x):
    return 100 <= abs(x) <= 999

data = [int(i) for i in open('446B6B.txt')]
mx = max(i for i in data if abs(i) % 100 == 17)
ans = []
for a, b, c in zip(data, data[1:], data[2:]):
    if tr(a) + tr(b) + tr(c) == 1:
        if a + b + c < mx:
            ans.append(a + b + c)
print(len(ans), max(ans))
