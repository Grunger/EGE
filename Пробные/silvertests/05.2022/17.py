a = list(map(int, open('17-04-1.txt').read().split()))
s = 0
for x in a:
    if x % 5 == 0:
        s += x % 10
k = 0
d = 10**10
for a, b in zip(a, a[1:]):
    if a * b % s == 0:
        k += 1
        d = min(d, (a - b) ** 2)
print(k, d)
