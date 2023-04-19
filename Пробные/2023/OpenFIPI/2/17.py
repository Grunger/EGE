f = [int(i) for i in open('17.txt').read().split()]
m = min(f)
ans = []
for a, b in zip(f, f[1:]):
    if a % 117 == m or b % 117 == m:
        ans.append(a + b)
print(len(ans), max(ans))
