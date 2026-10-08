a = list(map(int, open('17-04-1.txt').readlines()))

k = 0
m = 0
m3 = max(i for i in a if i % 6 == 0)
for a, b in zip(a, a[1:]):
    if a > m3 or b > m3:
        k += 1
        m = max(m, a + b)

print(k, m)
