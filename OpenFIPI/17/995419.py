def tr(x):
    return 10 <= abs(x) <= 99

data = [int(i) for i in open('995419.txt')]
mx = min(i for i in data if tr(i))
ans = []
for a, b in zip(data, data[1:]):
    if tr(a) + tr(b) == 1:
        if (a + b) % mx == 0:
            ans.append(a + b)
print(len(ans), max(ans))
