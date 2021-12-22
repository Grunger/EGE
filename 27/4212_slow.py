f = open('files/71/27-71a.txt')
n = int(f.readline())
data = list(map(int, f.readlines()))
m = 0
l = 0
for i in range(n):
    s = data[i]
    for j in range(i + 1, n):
        s += data[j]
        if s % 69 == 0:
            if s > m:
                m = s
                l = j - i + 1
            if s == m and j - i < l:
                l = j - i + 1
print(m, l)
