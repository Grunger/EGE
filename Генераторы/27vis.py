from turtle import *


def draw_grid(size, step):
    color("gray")

    # Draw vertical lines
    for x in range(-size, size + 1, step):
        penup()
        goto(x, -size)
        pendown()
        goto(x, size)

    # Draw horizontal lines
    for y in range(-size, size + 1, step):
        penup()
        goto(-size, y)
        pendown()
        goto(size, y)


tracer(0)
m = 50
dot(10, 'red')
draw_grid(400, m)
pu()

colors = ['red', 'green', 'blue']

with open('27A.txt') as f:
    edges = [(1, 5, 0, 4), (2, 6, 4, 8)]
    minx1, miny1, minx2, miny2 = 1000, 1000, 1000, 1000
    maxx1, maxy1, maxx2, maxy2 = -1000, -1000, -1000, -1000
    s = f.read().strip().replace(',', '.').split('\n')
    for line in s:
        x, y = map(float, line.split())
        if edges[0][0] <= x <= edges[0][1] and edges[0][2] <= y <= edges[0][3]:
            color = 'black'
            minx1 = min(minx1, x)
            miny1 = min(miny1, y)
            maxx1 = max(maxx1, x)
            maxy1 = max(maxy1, y)
        elif edges[1][0] <= x <= edges[1][1] and edges[1][2] <= y <= edges[1][3]:
            color = 'green'
            minx2 = min(minx2, x)
            miny2 = min(miny2, y)
            maxx2 = max(maxx2, x)
            maxy2 = max(maxy2, y)
        else:
            color = 'red'
        x *= m
        y *= m
        goto(x, y)
        dot(5, color)
print(f'{minx1=} {maxx1=} {miny1=} {maxy1=}')
print(f'{minx2=} {maxx2=} {miny2=} {maxy2=}')
done()


# with open('27B.txt') as f:
#     edges = [(-6.5, -1.5, 6.5, 11.5), (12.5, 17.5, 12.5, 17.5), (4.5, 9.5, 22.5, 27.5)]
#     s = f.read().strip().replace(',', '.').split('\n')
#     minx1, miny1, minx2, miny2, minx3, miny3 = 1000, 1000, 1000, 1000, 1000, 1000
#     maxx1, maxy1, maxx2, maxy2, maxx3, maxy3 = -1000, -1000, -1000, -1000, -1000, -1000
#     for line in s:
#         x, y = map(float, line.split())
#         if edges[0][0] <= x <= edges[0][1] and edges[0][2] <= y <= edges[0][3]:
#             color = 'black'
#             minx1 = min(minx1, x)
#             miny1 = min(miny1, y)
#             maxx1 = max(maxx1, x)
#             maxy1 = max(maxy1, y)
#         elif edges[1][0] <= x <= edges[1][1] and edges[1][2] <= y <= edges[1][3]:
#             color = 'green'
#             minx2 = min(minx2, x)
#             miny2 = min(miny2, y)
#             maxx2 = max(maxx2, x)
#             maxy2 = max(maxy2, y)
#         elif edges[2][0] <= x <= edges[2][1] and edges[2][2] <= y <= edges[2][3]:
#             color = 'blue'
#             minx3 = min(minx3, x)
#             miny3 = min(miny3, y)
#             maxx3 = max(maxx3, x)
#             maxy3 = max(maxy3, y)
#         else:
#             color = 'red'
#         x *= m
#         y *= m
#         goto(x, y)
#         dot(5, color)
# print(f'{minx1=} {maxx1=} {miny1=} {maxy1=}')
# print(f'{minx2=} {maxx2=} {miny2=} {maxy2=}')
# print(f'{minx3=} {maxx3=} {miny3=} {maxy3=}')
# done()

# minx1=-1.4142825804 maxx1=1.2916313694 miny1=-1.4739379899 maxy1=1.4549490644
# minx2=2.7581286477 maxx2=5.438739647 miny2=1.4777952492 maxy2=4.5571844025
# minx3=1.4520106362 maxx3=4.337450221 miny3=-4.4034239726 maxy3=-1.540252395
