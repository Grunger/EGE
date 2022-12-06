f = open('27_B.txt')
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
first_mx = data_mx[m]
mx = 0
print(data_mx)
for i in range(3 * m + 1, n - m):
    if data_mx[i] + first_mx > mx:
        mx = data_mx[i] + first_mx
    first_mx = max(first_mx, data_mx[i - 2 * m])
print(mx)
# 11749
