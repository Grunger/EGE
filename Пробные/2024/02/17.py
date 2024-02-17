a = [int(i) for i in open('17.txt').read().split()]
ans = []
m22 = max(i for i in a if i % 117 == 0)
for x1, x2, x3 in zip(a, a[1:], a[2:]):
    if (10000 <= x1 <= 99999) + (10000 <= x2 <= 99999) + (10000 <= x3 <= 99999) == 2 and x1 + x2 + x3 <= m22:
        ans.append(x1 + x2 + x3)
print(len(ans), max(ans))
