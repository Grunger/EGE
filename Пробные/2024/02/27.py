f = open('27_T.txt')
k = int(f.readline())
n = int(f.readline())
a = [int(i) for i in f]
m = 0
for i in range(n):
    for j in range(i + k, n):
        for w in range(j + k, n):
            s = a[i] + a[j] + a[w]
            if s % 2 == 1 and s > m:
                m = s
print(m)

# 185463