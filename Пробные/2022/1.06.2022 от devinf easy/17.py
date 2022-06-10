a = list(map(int, open('17-04-1.txt').readlines()))

k = 0
m = 10**9
m22 = max(i for i in a if i % 22 == 0)
for a, b in zip(a, a[1:]):
    if a > m22 or b > m22:
        k += 1
        m = min(m, a + b)

print(k, m)