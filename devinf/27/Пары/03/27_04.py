f = open('27_A.txt')
n = int(f.readline())
a = [int(i) for i in f]
mx = 0
for i in range(n):
    for j in range(i + 1, n):
        if (a[i] + a[j]) % 120 == 0 and (a[i] > a[j]):
            mx = max(mx, a[i] + a[j])
print(mx)
