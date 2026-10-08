from turtle import *

f = open('27B.txt').read().strip().replace(',', '.').split('\n')
points = []
for line in f:
    x, y = map(float, line.split())
    points.append((x, y))
cl = [[], [], []]
for p in points:
    x, y = p
    if x**2 + y ** 2 > 4 and y < x + 2 and y > -3 and x < 0:
        cl[0].append(p)
    elif x**2 + y ** 2 < 4 and y > x + 2:
        cl[1].append(p)
    elif x**2 + y ** 2 < 4 and x > 1:
        cl[2].append(p)


centers = []
for c in cl:
    mn = 10**10
    cen = 0
    for p1 in c:
        x1, y1 = p1
        s = 0
        for p2 in c:
            x2, y2 = p2
            s += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        if s < mn:
            mn = s
            cen = p1
    centers.append(cen)
#
print((centers[0][0] + centers[1][0] + centers[2][0]) / 3 * 10000)
print((centers[0][1] + centers[1][1] + centers[2][1]) / 3 * 10000)
#
# -6962.005698582856
# -2966.9443728192596
# 6962  2966
print(len(cl[0]))
print(len(cl[1]))
print(len(cl[2]))
m = 100
pu()
tracer(0)
for p in cl[0]:
    x, y = p
    goto(x * m, y * m)
    dot(3, 'blue')
for p in cl[1]:
    x, y = p
    goto(x * m, y * m)
    dot(3, 'purple')
for p in cl[2]:
    x, y = p
    goto(x * m, y * m)
    dot(3, 'green')
for c in centers:
    x, y = c
    goto(x * m, y * m)
    dot(10, 'red')
done()