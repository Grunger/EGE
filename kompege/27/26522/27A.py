f = open('27A.txt').read().strip().replace(',', '.').split('\n')
points = []
for line in f:
    x, y = map(float, line.split())
    points.append((x, y))
cl = [[], []]
for p in points:
    x, y = p
    if y < x and y > x ** 2 - 3 and x < 0:
        cl[0].append(p)
    elif y < x and y > x ** 2 - 3 and y > 0:
        cl[1].append(p)


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

print((centers[0][0] + centers[1][0]) / 2 * 10000)
print((centers[0][1] + centers[1][1]) / 2 * 10000)

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