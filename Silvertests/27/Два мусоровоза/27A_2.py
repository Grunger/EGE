f = open('107_27_B.txt')
n = int(f.readline())
data = list(map(int, f.readlines()))
# print(data)

m = 10**9
for i in range(n):
    s1 = 0
    s2 = 0
    data1 = data[1: n // 2 + 1]
    data2 = data[:n // 2:-1]
    for j in range(n // 2):
        s1 += data1[j] * (j + 1)
        s2 += data2[j] * (j + 1)
    if max(s1, s2) < m:
        print(i, s1, s2)
        m = max(s1, s2)
        ans = i + 1
    data = data[1:] + [data[0]]
print(m, ans)
