f = open('26_1395_kab.txt')
s, n = map(int, f.readline().split())
data = sorted(map(int, f.readlines()))
print(s, n)
print(data)

s1 = 0
for i in range(n):
    s1 += data[i]
    if s1 > s:
        print(i + 1, s1)
        print(i, s1 - data[i])
        break
