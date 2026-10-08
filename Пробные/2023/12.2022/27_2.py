f = open('27_0.txt')
n, m = map(int, f.readline().split())
data = [int(i) for i in f]
capacity = 6
data_k = [i // capacity + bool(i % capacity) for i in data]
data_mx = [0] * n
mx = 0
for i in range(2 * m + 1):
    mx += data_k[i]
data_mx[m] = mx
for i in range(m + 1, n - m):
    mx -= data_k[i - m - 1]
    mx += data_k[i + m]
    data_mx[i] = mx
for first in range(m, n - 3 * m - 1):
    for second in range(first + 2 * m + 1, n - m):
        # 3750000
        if first % 100000 == 0:
            print(first, second, data_mx[first] + data_mx[second], mx)
        mx = max(mx, data_mx[first] + data_mx[second])
print(mx)
# 11749
