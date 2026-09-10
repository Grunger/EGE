f = open('27-A.txt')
n = int(f.readline())
a = [int(i) for i in f]
k = 0
r = 321
for i in range(n):
    for j in range(i, n):
        if sum(a[i:j + 1]) % r == 0:
            k += 1
print(k)
