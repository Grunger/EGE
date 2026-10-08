import re

def dist(x1, y1, x2, y2):
    return abs(x2-x1)+abs(y2-y1)

f = open('1_27_A.txt')
s = []
for line in f:
    x, y, t = line.split()
    x = float(x.replace(',', '.'))
    y = float(y.replace(',', '.'))
    s.append([x, y, t])
clusters = [[], []]
for p1 in s:
    x, y, t = p1
    if y > 15:
        clusters[0].append([x, y, t])
    else:
        clusters[1].append([x, y, t])
# print(len(clusters[0]), len(clusters[1]))
# 121 114

cen = []
for i in range(2):
    mn = 10**10
    for p1 in clusters[i]:
        x1, y1, t1 = p1
        s = 0
        for p2 in clusters[i]:
            x2, y2, t2 = p2
            d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            s += d
        if s < mn:
            mn = s
            cn = p1
    cen.append(cn)
# print(cen)
# [[7.717373, 20.05071, 'B6IV'], [4.960398, 7.34545, 'O8I']]

mx = 0
for p1 in clusters[1] + clusters[0]:
    x1, y1, t1 = p1
    if re.search(r'^G.V$', t1):
        d = dist(x1, y1, 4.960398, 7.34545)
        if d > mx:
            mx = d
            cn = p1
print(cn[0] * 10000)
print(cn[1] * 10000)
