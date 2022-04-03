a = list(map(int, open('17-1.txt').readlines()))

k = 0
m = 0
for i in range(len(a) - 1):
    x, y = abs(a[i]), abs(a[i + 1])
    if (x % 5 == 0 and y % 7 == 0 or x % 7 == 0 and y % 5 == 0) and x % 3 and y % 3:
        k += 1
        m = max(m, a[i] + a[i + 1])
print(k, m)
