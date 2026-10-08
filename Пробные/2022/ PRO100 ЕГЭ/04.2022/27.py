f = open('27-1A.txt')
n, k = map(int, f.readline().split())
data = [int(i) for i in f]
m = 10**10
for i in range(n):
    for j in range(i, n):
        if len(set(data[i:j + 1])) == k:
            m = min(m, j - i + 1)
print(m)
