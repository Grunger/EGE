from turtle import * 

with open('27-Б.txt') as f:
    dots = f.read().replace(',', '.').strip().split('\n')
    for i in range(len(dots)):
        dots[i] = [float(d) for d in dots[i].split()]
clusters = [[], [], []]
for d in dots:
    x, y = d
    if y > x + 2 and x**2 + y ** 2 < 4:
        clusters[0].append(d)
    elif x > 1 and x**2 + y ** 2 < 4:
        clusters[1].append(d)
    elif x**2 + y ** 2 > 4 and y > -3 and y < x + 2 and x < 0:
        clusters[2].append(d)
pu()
tracer(0)
colors = ['red', 'green', 'blue']
for i in range(3):
    c = clusters[i]
    for d in c:
        x, y = d
        goto(int(x * 100), int(y * 100))
        dot(3, colors[i])
done()

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
    print(center)
    s_x += center[0]
    s_y += center[1]
print(s_x / 3 * 10000)
print(s_y / 3 * 10000)

# -6962.005698582855
# -2966.9443728192596
# 6962 2966
