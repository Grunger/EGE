f = open('27_A.txt')
k = int(f.readline())
n = int(f.readline())
a = [int(i) for i in f]
mx = 0
for i in range(n):
    for j in range(i + k, n):
        if (a[i] % 26 == 0 or a[j] % 26 == 0) and (a[i] - a[j]) % 2 != 0:
            print(a[i], a[j])
            mx = max(mx, a[i] + a[j])
print(mx)
#1583