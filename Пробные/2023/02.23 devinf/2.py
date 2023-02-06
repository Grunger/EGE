from itertools import product

print('x y z w')
for x, y, z, w in product((0, 1), repeat=4):
    f = (w != y) or (((not x) <= z) and ((not w) <= y))
    if not f:
        print(x, y, z, w)
