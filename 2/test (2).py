from itertools import product


print('w x y z, f')
for w, x, y, z in product((0, 1), repeat=4):
    f = ((w or x) <= (not(y) or z)) == (not(w) and y)
    if f:
        print(w, x, y, z, f)