from turtle import *
tracer(0)
pu()
m = 15

f = open('8. 27B.txt')
a = f.read().strip().replace(',', '.').split('\n')
a = [[float(i) for i in j.split()] for j in a]
# x > 5 y < 5
c = [[], [], []]
anomaly = []

minx1, miny1, minx2, miny2, minx3, miny3 = 1000, 1000, 1000, 1000, 1000, 1000
maxx1, maxy1, maxx2, maxy2, maxx3, maxy3 = -1000, -1000, -1000, -1000, -1000, -1000
for p in a:
    x, y = p
    if x < 0:
        c[2].append(p)
        minx3 = min(x, minx3)
        miny3 = min(y, miny3)
        maxx3 = max(x, maxx3)
        maxy3 = max(y, maxy3)
    elif y > 20:
        c[1].append(p)
        minx2 = min(minx2, x)
        miny2 = min(miny2, y)
        maxx2 = max(maxx2, x)
        maxy2 = max(maxy2, y)
    elif 11 < x < 18:
        c[0].append(p)
        minx1 = min(minx1, x)
        miny1 = min(miny1, y)
        maxx1 = max(maxx1, x)
        maxy1 = max(maxy1, y)
    else:
        anomaly.append(p)

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


print(minx1, miny1, minx2, miny2, minx3, miny3)
print(maxx1, maxy1, maxx2, maxy2, maxx3, maxy3)

print((maxx1 - minx1) * (maxy1 - miny1))
print((maxx2 - minx2) * (maxy2 - miny2))
print((maxx3 - minx3) * (maxy3 - miny3))

# 3228 3287 3241

qx = ((cen[2][0] - cen[0][0]) ** 2 + (cen[2][1] - cen[0][1]) ** 2) ** 0.5

qy = 0
for p in cen:
    x1, y1 = p
    for p1 in anomaly:
        x2, y2 = p1
        qy = max(qy, ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5)

print(qx * 10000, qy * 10000)
# 199093.5994725694 300212.8684195366
# 199093 300212
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
for p in anomaly:
    x, y = p
    goto(x * m, y * m)
    dot(10, 'purple')
done()
