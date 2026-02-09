from turtle import *


with open('27-A.txt') as f:
    dots = f.read().replace(',', '.').strip().split('\n')
    for i in range(len(dots)):
        dots[i] = [float(d) for d in dots[i].split()]
clusters = [[], []]
for d in dots:
    x, y = d
    if y > x ** 2 - 3 and y < x and x < 0:  # под параболой, над y=x и ниже нуля по у
        clusters[0].append(d)
    elif y > 0 and y > x ** 2 - 3 and y < x:  # под параболой, над y=x и правее x
        clusters[1].append(d)
s_x, s_y = 0, 0
for c in clusters:
    mn = 10**10
    for p1 in c:
        x1, y1 = p1
        s = 0
        for p2 in c:
            x2, y2 = p2
            d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
            s += d
        if s < mn:
            mn = s
            center = p1
    s_x += center[0]
    s_y += center[1]
    print(center)
print(s_x / 2 * 10000)
print(s_y / 2 * 10000)
pu()
tracer(0)
colors = ['red', 'green', 'blue']
for i in range(2):
    c = clusters[i]
    for d in c:
        x, y = d
        goto(int(x * 100), int(y * 100))
        dot(5, colors[i])
done()

# 4524.771697479702
# -4738.833100223753
# 4524 4738
