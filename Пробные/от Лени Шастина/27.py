f = open('270.txt')
n, k, d = map(int, f.readline().split())
m = 0
data = list(map(int, f.readlines()))
for i in range(n):
    for j in range(i, n):
        s1 = sum(data[i:j + 1])
        s2 = sum(data[:i]) + sum(data[j + 1:])
        if s1 % k == 0 and s2 % d == 0 and (n - j + 1 - i) % 2 == 1:
            m = max(m, s1)
            print(m)
print(m)
