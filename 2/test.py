from itertools import product


print('w x y z, f')
for w, x, y, z in product((0, 1), repeat=4):
    f = (x and z) or ((w <= x) == (z <= y))
    if not f:
        print(w, x, y, z)
