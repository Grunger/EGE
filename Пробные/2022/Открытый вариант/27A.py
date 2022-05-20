f = open('107_27_A.txt')
n = int(f.readline())
data = list(map(int, f.readlines()))
data = data[n // 2:] + data + data[:n // 2]
m = 10**9
for i in range(n // 2, n // 2 + n):
    s = 0
    for j in range(n // 2 + 1):
        s += data[i + j] * j
        if j != n // 2:
            s += data[i - j] * j
    if s < m:
        m = s
        ans = i + 1 - n // 2
print(m * 3, ans)
