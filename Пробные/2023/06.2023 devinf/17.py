a = [int(i) for i in open('17.txt').read().split()]
mx2 = max(i for i in a if 10 <= abs(i) <= 99)
print(mx2)
ans = []
for x, y in zip(a, a[1:]):
    if (10 <= abs(x) <= 99 or 10 <= abs(y) <= 99) and x + y <= mx2:
        ans.append(x + y)
print(len(ans), max(ans))

