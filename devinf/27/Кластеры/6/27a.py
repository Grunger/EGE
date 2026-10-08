from turtle import *
tracer(0)
pu()
m = 40

f = open('6. 27A.txt')
a = f.read().strip().replace(',', '.').split('\n')
a = [[float(i) for i in j.split()] for j in a]
# y = 6
c = [[], []]
for p in a:
    x, y = p
    c[int(x > 0)].append(p)

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

px = (cen[0][0] + cen[1][0]) / 2
py = (cen[0][1] + cen[1][1]) / 2
print(px * 10000, py * 10000)
# 5061.7754575 65220.09561599999
# 5061 65220

colors = ['red', 'green', 'blue']
d = 300
for i in range(2):
    for p in c[i]:
        x, y = p
        goto(x * m - d, y * m)
        dot(5, colors[i])
for p in cen:
    x, y = p
    goto(x * m - d, y * m)
    dot(10, 'purple')
done()