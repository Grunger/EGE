from turtle import *
tracer(0)
pu()
m = 40

f = open('3. 27B.txt')
a = f.read().strip().replace(',', '.').split('\n')
a = [[float(i) for i in j.split()] for j in a]
# x > 5 y < 5
c = [[], [], []]
for p in a:
    x, y = p
    if x >= 2 and y > 0:
        c[2].append(p)
    elif x >= 1.5 or y < -2:
        c[1].append(p)
    else:
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
# 3208 3225 3293
qx = cen[0][0] - cen[2][0]
qy = cen[0][1] - cen[2][1]
print(qx * 10000, qy * 10000)
# -39930.733394 -29845.890096
# 39930 29845
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