from turtle import *
tracer(0)
pu()
m = 40

f = open('5. 27B.txt')
a = f.read().strip().replace(',', '.').split('\n')
a = [[float(i) for i in j.split()] for j in a]
# x > 5 y < 5
c = [[], [], []]
for p in a:
    x, y = p
    if x > 2 and y > 3:
        c[2].append(p)
    elif x > 1 and y < -3:
        c[1].append(p)
    elif x < 3 and -3 < y < 3:
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
# 3278 3276 3230
qx = ((cen[0][0] - cen[2][0]) ** 2 + (cen[0][1] - cen[2][1]) ** 2) ** 0.5
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
# 100413.37009138719 41440.70909745937
# 70428 41440
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