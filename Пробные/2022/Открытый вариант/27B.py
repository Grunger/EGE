f = open('107_27_B.txt')
n = int(f.readline())
data = list(map(int, f.readlines()))

sm = sum(data)

s = [0] * n
for i in range(n // 2):
    s[0] += data[i]
for i in range(1, n):
    s[i] = s[i - 1] - data[i - 1] + data[(n // 2 + i - 1) % n]

p = [0] * n
for i in range(n):
    p[i] = sm - s[i]
# print(data)
# print(s)
# print(p)

maxs = 0
for j in range(n // 2 + 1):
    maxs += data[j] * j
    if j != n // 2:
        maxs += data[-j] * j
ans = 0
mx = maxs
for i in range(1, n):
    maxs -= s[i]
    maxs += p[i]
    # print(i, maxs)
    if maxs < mx:
        mx = maxs
        ans = i
print(mx * 3, ans + 1)
