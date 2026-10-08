# Авторы: PRO100 ЕГЭ

f = open('27-98b.txt')
n, k = [int(x) for x in f.readline().split()]
a = [0] * n
for i in range(n):
    a[i] = int(f.readline())
m = [0] * (k + 1)
l = 0
r = 0
m[a[0]] += 1
d = 10000000000
while r < n:
    while m.count(0) != 1:
        r += 1
        if r == n:
            break
        m[a[r]] += 1
    while m.count(0) == 1:
        if r - l + 1 < d:
            d = r - l + 1
        m[a[l]] -= 1
        l += 1
print(d)
# Видеоразбор
# https://youtu.be/y7N-5jX99X0?t=15793



