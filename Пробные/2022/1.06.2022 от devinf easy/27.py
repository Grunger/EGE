f = open('27A.txt')
n, m = map(int, f.readline().split())
a = []
for i in range(n):
    a.append(int(f.readline()))
a.sort()
penalty = 0
s = 0
for k in range(1, n + 1):
    b = a[k - 1::-1]
    for j in range(len(b)):
        penalty += b[j] * (j // m + 1)
print(penalty)
