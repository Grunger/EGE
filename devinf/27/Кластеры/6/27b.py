from turtle import *
tracer(0)
pu()
m = 15

f = open('6. 27B.txt')
a = f.read().strip().replace(',', '.').split('\n')
a = [[float(i) for i in j.split()] for j in a]
# x > 5 y < 5
c = [[], [], []]
for p in a:
    x, y = p
    if 10 < x < 18 and y > 10:
        c[2].append(p)
    elif x > 20 and y < 8:
        c[1].append(p)
    elif x < 10 and y < 12:
        c[0].append(p)

cen = []
for i in range(3):
    mn = 10**10
    cn = 0
    for p1 in c[i]:
        x1, y1 = p1
        s = 0
        for p2 in c[i]:
            x2, y2 = p2
            d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            s += d
        if s < mn:
            mn = s
            cn = p1
    cen.append(cn)


print(len(c[0]), len(c[1]), len(c[2]))
# 3228 3287 3241
qx = max(((cen[1][0] - cen[2][0]) ** 2 + (cen[1][1] - cen[2][1]) ** 2) ** 0.5,
         ((cen[0][0] - cen[1][0]) ** 2 + (cen[0][1] - cen[1][1]) ** 2) ** 0.5,
         ((cen[0][0] - cen[2][0]) ** 2 + (cen[0][1] - cen[2][1]) ** 2) ** 0.5)
qy = -10**10
for p in c[0]:
    x1, y1 = p
    if p == cen[0]:
        continue
    qy = max(qy, ((cen[0][0] - x1) ** 2 + (cen[0][1] - y1) ** 2) ** 0.5)
for p in c[1]:
    x1, y1 = p
    if p == cen[1]:
        continue
    qy = max(qy, ((cen[1][0] - x1) ** 2 + (cen[1][1] - y1) ** 2) ** 0.5)
for p in c[2]:
    x1, y1 = p
    if p == cen[2]:
        continue
    qy = max(qy, ((cen[2][0] - x1) ** 2 + (cen[2][1] - y1) ** 2) ** 0.5)


print(qx * 10000, qy * 10000)
# 203751.58516227247 28795.694864343975
# 203751 28795
colors = ['red', 'green', 'blue']
for i in range(3):
    for p in c[i]:
        x, y = p
        goto(x * m, y * m)
        dot(5, colors[i])
for p in cen:
    x, y = p
    goto(x * m, y * m)
    dot(10, 'purple')
done()