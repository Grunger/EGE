from itertools import product

print('y x z w')
for w, x, y, z in product((0, 1), repeat=4):
    f = (x or y) and (x <= (not z)) and not w
    if f:
        print(x, z, y, w)