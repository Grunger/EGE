import re

def dist(x1, y1, x2, y2):
    return abs(x2-x1)+abs(y2-y1)

f = open('1_27_B.txt')
s = []
for line in f:
    x, y, t = line.split()
    x = float(x.replace(',', '.'))
    y = float(y.replace(',', '.'))
    s.append([x, y, t])
clusters = [[], [], []]
for p1 in s:
    x, y, t = p1
    if y < 30:
        clusters[0].append([x, y, t])
    elif x > 16:
        clusters[1].append([x, y, t])
    else:
        clusters[2].append([x, y, t])
# print(len(clusters[0]), len(clusters[1]))
# 121 114

cen = []
for i in range(3):
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
# [[11.746691, 24.957689, 'F2I'], [18.794456, 36.905542, 'B1III'], [13.223572, 36.619979, 'M3III']]
kk = []
for i in range(3):
    k = 0
    for p1 in clusters[i]:
        x1, y1, t1 = p1
        if re.search(r'^O', t1):
            k += 1
    kk.append(k)
# print(kk)
# [165, 43, 68]
print(dist(11.746691, 24.957689, 18.794456, 36.905542) * 10000)
for i in range(3):
    y = []
    for p1 in clusters[i]:
        x1, y1, t1 = p1
        if re.search(r'^G.V$', t1):
            y.append(p1)

    mx = 0
    for d1 in y:
        x1, y1, t1 = d1
        for d2 in y:
            x2, y2, t2 = d2
            mx = max(mx, dist(x1, y1, x2, y2))
    # print(mx)
print(4.615407999999999 * 10000)