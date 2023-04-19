f = [int(i) for i in open('17.txt').read().split()]
m = min(f)
ans = []
for a, b in zip(f, f[1:]):
    if a % 111 == m or b % 111 == m:
        ans.append(a + b)
print(len(ans), min(ans))
