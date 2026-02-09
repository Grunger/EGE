from turtle import *
tracer(0)
pu()
m = 60

f = open('1. 27_A.txt')
a = f.read().strip().replace(',', '.').split('\n')
a = [[float(i) for i in j.split()] for j in a]
x = 1
c = [[], []]
for p in a:
    x, y = p
    c[int(x > 1)].append(p)

cen = []
for i in range(2):
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


for i in range(2):
    px, py = 0, 0
    xc, yc = cen[i]
    for p in c[i]:
        x, y = p
        if abs(x - xc) > px:
            px = abs(x - xc)
        if abs(y - yc) > py:
            py = abs(y - yc)
    print(px * 10000, py * 10000)
# 14749.9690605735 14299.871539513504
# 14749 14299

colors = ['red', 'green', 'blue']
for i in range(2):
    for p in c[i]:
        x, y = p
        goto(x * m, y * m)
        dot(5, colors[i])
for p in cen:
    x, y = p
    goto(x * m, y * m)
    dot(10, 'purple')
done()