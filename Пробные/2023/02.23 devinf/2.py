from itertools import product

print('y x w z')
for x, y, z, w in product((0, 1), repeat=4):
    f = (w == y) or ((not x <= z) and ((not z) <= y))
    if not f:
        print(y, x, w, z)
