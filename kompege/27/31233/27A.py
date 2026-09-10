f = open('27_A_31233.txt').read().strip().replace(',', '.').split('\n')
points = []
for line in f:
    x, y, t = line.split()
    x = float(x)
    y = float(y)
    points.append((x, y, t))
cl = [[], []]
for p in points:
    x, y, t = p
    if y > x:
        cl[0].append(p)
    else:
        cl[1].append(p)


centers = []
for c in cl:
    mn = 10**10
    cen = 0
    for p1 in c:
        x1, y1, t1 = p1
        s = 0
        for p2 in c:
            x2, y2, t2 = p2
            s += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        if s < mn:
            mn = s
            cen = p1
    centers.append(cen)
print(centers)

# 4524.771697479702
# -4738.833100223753
# 4524  4738
# print(len(cl[0]))
# print(len(cl[1]))
# m = 100
# pu()
# tracer(0)
# for p in cl[0]:
#     x, y = p
#     goto(x * m, y * m)
#     dot(3, 'blue')
# for p in cl[1]:
#     x, y = p
#     goto(x * m, y * m)
#     dot(3, 'purple')
# for c in centers:
#     x, y = c
#     goto(x * m, y * m)
#     dot(10, 'red')
# done()