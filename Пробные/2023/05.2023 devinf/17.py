a = [int(i) for i in open('17.txt').readlines()]
ans = []
mx3 = max(i for i in a if 100 <= i <= 999)
for x, y in zip(a, a[1:]):
    if (100 <= abs(x) <= 999) != (100 <= abs(y) <= 999) and x + y <= mx3:
        ans.append(x + y)
print(len(ans), max(ans))

ma = -99999999
for i in range(len(a)):
    if len(str(a[i])) == 3:
        ma = max(ma, a[i])
k = 0
maxi = -9999999
for i in range(len(a) - 1):
    if ((99 < abs(a[i]) < 1000 and not (99 < abs(a[i + 1]) < 1000)) or (
            not (99 < abs(a[i]) < 1000) and 99 < abs(a[i + 1]) < 1000)) and (a[i] + a[i + 1]) <= ma:
        k += 1
        maxi = max(maxi, a[i] + a[i + 1])
print(k, maxi)

k = 0
maxi = -9999999
for i in range(len(a) - 1):
    if (99 < abs(a[i]) < 1000 or 99 < abs(a[i + 1]) < 1000) and (a[i] + a[i + 1]) <= ma:
        k += 1
        maxi = max(maxi, a[i] + a[i + 1])
print(k, maxi)
