a = [int(i) for i in open('17_16-17.txt').read().split()]
ans = []
m = max(i for i in a if 100 <= i <= 999 and i % 100 == 12)
for a, b, c in zip(a, a[1:], a[2:]):
    if (100 <= a <= 999) + (100 <= b <= 999) + (100 <= c <= 999) <= 2:
        if a + b + c >= m:
            ans.append(a + b + c)
print(len(ans), min(ans))
