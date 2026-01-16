def tr(x):
    return 1000 <= abs(x) <= 9999

data = [int(i) for i in open('FA6c24.txt')]
mx = max(i for i in data if abs(i) % 100 == 25)
ans = []
for a, b, c in zip(data, data[1:], data[2:]):
    if tr(a) + tr(b) + tr(c) <= 2:
        if a + b + c < mx:
            ans.append(a + b + c)
print(len(ans), max(ans))
