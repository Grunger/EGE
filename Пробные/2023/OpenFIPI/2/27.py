f = open('27_A.txt')
n, m = map(int, f.readline().split())

count = 1000
data = [0] * 1000
for line in f:
    i, j = map(int, line.split())
    data[i] = j
mx = 0  # рейсы
mx_send = 0  # отправления
for i in range(m + 1, 1000 - m):
    k = 0
    k_send = 0
    for j in range(i, i - m - 1, -1):
        k_send += data[j]
        k += data[j] // 30 + bool(data[j] % 30)
    for j in range(i + 1, i + m + 1):
        k_send += data[j]
        k += data[j] // 30 + bool(data[j] % 30)
    if k_send > mx_send:
        mx_send = k_send
        mx = k
    elif k_send == mx_send and k < mx:
        mx = k
print(mx)
