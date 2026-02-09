from random import randint, gauss, shuffle

dot = 10
# x1 x2 y1 y2

# with open('27A.txt', 'w') as f:
#     r = []
#     edges = [(1, 5, 0, 4), (2, 6, 4, 8)]
#     for c in edges:
#         for i in range(randint(450, 500)):
#             x = gauss((c[0] + c[1]) / 2, abs(c[0] - c[1]) / 10)
#             y = gauss((c[2] + c[3]) / 2, abs(c[2] - c[3]) / 10)
#             if c[0] <= x <= c[1] and c[2] <= y <= c[3]:
#                 r.append((x, y))
#     shuffle(r)
#     for x, y in r:
#         f.write(f'{x:.10f}\t{y:.10f}\n'.replace('.', ','))

# with open('27B.txt', 'w') as f:
#     r = []
#     edges = [(-6.5, -1.5, 6.5, 11.5), (12.5, 17.5, 12.5, 17.5), (4.5, 9.5, 22.5, 27.5)]
#     for c in edges:
#         for i in range(randint(3200, 3300)):
#             x = gauss((c[0] + c[1]) / 2 + randint(-1, 1), abs(c[0] - c[1]) / 10)
#             y = gauss((c[2] + c[3]) / 2, abs(c[2] - c[3]) / 10)
#             if c[0] <= x <= c[1] and c[2] <= y <= c[3]:
#                 r.append((x, y))
#     # аномалии
#     x = 25.123134445123
#     y = 16.134534555123
#     r.append((x, y))
#     x = 4.21354321344
#     y = 17.123652156434
#     r.append((x, y))
#     x = 10.56412476767
#     y = 3.1484823544
#     r.append((x, y))
#
#     shuffle(r)
#     for x, y in r:
#         f.write(f'{x:.10f}\t{y:.10f}\n'.replace('.', ','))
