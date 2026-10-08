f = open('26134.txt')
n, d = map(int, f.readline().split())
# d = 131
# d = 129
s = {
    0: [],
    1: []
}
for line in f:
    c, t = map(int, line.split())
    s[t].append(c)
s[0].sort()
s[1].sort()
# 30
a = [s[0][30]]
i0 = 0
i1 = 0
while i0 < len(s[0]) and i1 < len(s[1]):
    while i1 < len(s[1]) and s[1][i1] < a[-1] + d:
        i1 += 1
    if i1 < len(s[1]):
        a.append(s[1][i1])
    while i0 < len(s[0]) and s[0][i0] < a[-1] + d:
        i0 += 1
    if i0 < len(s[0]):
        a.append(s[0][i0])
print(len(a))
a = [s[1][32]]
i0 = 0
i1 = 0
while i0 < len(s[0]) and i1 < len(s[1]):
    while i0 < len(s[0]) and s[0][i0] < a[-1] + d:
        i0 += 1
    if i0 < len(s[0]):
        a.append(s[0][i0])
    while i1 < len(s[1]) and s[1][i1] < a[-1] + d:
        i1 += 1
    if i1 < len(s[1]):
        a.append(s[1][i1])
print(len(a))
