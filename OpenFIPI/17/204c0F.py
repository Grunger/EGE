def tr(x):
    return 10000 <= abs(x) <= 99999

data = [int(i) for i in open('204c0F.txt')]
mx = max(i for i in data if abs(i) % 100 == 27)
ans = []
for a, b, c in zip(data, data[1:], data[2:]):
    if tr(a) + tr(b) + tr(c) >= 1:
        if a + b + c >= mx:
            ans.append(a + b + c)
print(len(ans), max(ans))
