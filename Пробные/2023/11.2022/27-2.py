f = open('27_B.txt')
n, m = map(int, f.readline().split())

point = dict()
w = [0] * 10**8
for _ in range(n):
    i, j = map(int, f.readline().split())
    point[i] = j
    w[i] = j // 50 + bool(j % 50)
start = min(point)
k = 0
k_send = 0
for j in range(start, start - m, -1):
    if j < 0:
        break
    k_send += point.get(j, 0)
    k += w[j]
for j in range(start + 1, start + m + 1):
    k_send += point.get(j, 0)
    k += w[j]
mx = k
mx_send = k_send
for i in range(start + 1, max(point) + 1):
    k -= w[i - m - 1]
    k += w[i + m]
    k_send -= point.get(i - m - 1, 0)
    k_send += point.get(i + m, 0)
    if i not in point:
        continue
    if k_send > mx_send:
        mx_send = k_send
        mx = k
    elif k_send == mx_send and k < mx:
        mx = k
print(mx)
