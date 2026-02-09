from turtle import *
tracer(0)
pu()
m = 15

f = open('7. 27B.txt')
a = f.read().strip().replace(',', '.').split('\n')
a = [[float(i) for i in j.split()] for j in a]
# x > 5 y < 5
c = [[], [], []]
for p in a:
    x, y = p
    if x < 0:
        c[2].append(p)
    elif y > 20:
        c[1].append(p)
    elif 11 < x < 18:
        c[0].append(p)

cen = []
for i in range(3):
    mn = 10**10
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
# 3290 3242 3290

qx = -10**10
for p in c[0]:
    x1, y1 = p
    if p == cen[0]:
        continue
    qx = max(qx, ((cen[0][0] - x1) ** 2 + (cen[0][1] - y1) ** 2) ** 0.5)
for p in c[1]:
    x1, y1 = p
    if p == cen[1]:
        continue
    qx = max(qx, ((cen[1][0] - x1) ** 2 + (cen[1][1] - y1) ** 2) ** 0.5)
for p in c[2]:
    x1, y1 = p
    if p == cen[2]:
        continue
    qx = max(qx, ((cen[2][0] - x1) ** 2 + (cen[2][1] - y1) ** 2) ** 0.5)

qy = 10**10
for p in c[1] + c[2]:
    x1, y1 = p
    qy = min(qy, ((cen[0][0] - x1) ** 2 + (cen[0][1] - y1) ** 2) ** 0.5)
for p in c[0] + c[2]:
    x1, y1 = p
    qy = min(qy, ((cen[1][0] - x1) ** 2 + (cen[1][1] - y1) ** 2) ** 0.5)
for p in c[0] + c[1]:
    x1, y1 = p
    qy = min(qy, ((cen[2][0] - x1) ** 2 + (cen[2][1] - y1) ** 2) ** 0.5)

print(qx * 10000, qy * 10000)
# 27229.056418355434 101388.8285050559
# 27229 101388
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