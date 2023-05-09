a = [int(i) for i in open('17.txt').readlines()]
ans = []
mx3 = max(i for i in a if 100 <= i <= 999)
for x, y in zip(a, a[1:]):
    if (100 <= abs(x) <= 999) != (100 <= abs(y) <= 999) and x + y <= mx3:
        ans.append(x + y)
print(len(ans), max(ans))
