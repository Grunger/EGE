from itertools import product

print('y z w x')
for w, x, y, z in product((0, 1), repeat=4):
    f = ((x <= y) == (z and w)) and (x <= z)
    if f:
        print(y, z, w, x)

