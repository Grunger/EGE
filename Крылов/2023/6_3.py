from math import cos, sin, radians


def line1(x):
    # 1 - 2
    return (x - x1) * (y2 - y1) / (x2 - x1) + y1


def line2(x):
    # 2 - 3
    return (x - x2) * (y3 - y2) / (x3 - x2) + y2


def line3(x):
    # 3 - 4
    return (x - x3) * (y4 - y3) / (x4 - x3) + y3


def line4(x):
    # 1 - 4
    return (x - x1) * (y4 - y1) / (x4 - x1) + y1


x1 = 100
y1 = 100
x2 = 100 + 30 * cos(radians(30))
y2 = 100 - 30 * sin(radians(30))
x3 = 100 - 40 * cos(radians(60)) + 30 * cos(radians(30))
y3 = 100 - 30 * sin(radians(30)) - 40 * sin(radians(60))
x4 = 100 - 40 * cos(radians(60))
y4 = 100 - 40 * sin(radians(60))
k = 0
for x in range(500):
    for y in range(500):
        if line1(x) > y > line3(x) and line2(x) < y < line4(x):
            k += 1
print(k)
