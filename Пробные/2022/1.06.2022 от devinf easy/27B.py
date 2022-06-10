f = open('27B.txt')
n, m = map(int, f.readline().split())
a = []
for i in range(n):
    a.append(int(f.readline()))
a.sort()

penalty = 0
for i in range(n):
    penalty += a[i]
    a[i] = penalty
    if i >= m:
        a[i] += a[i - m]
print(a[k - 1])