f = open('27_A.txt')
n, m = map(int, f.readline().split())
data = [int(i) for i in f]
capacity = 6
data_k = [i // capacity + bool(i % capacity) for i in data]
mx = 0
for first in range(m, n - 3 * m - 1):
    for second in range(first + 2 * m + 1, n - m):
        k = 0
        for i in range(first - m, first + m + 1):
            k += data_k[i]
        for i in range(second - m, second + m + 1):
            k += data_k[i]
        print(first, second, k, mx)
        mx = max(mx, k)
print(mx)
# 11749