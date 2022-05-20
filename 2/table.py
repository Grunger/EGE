from itertools import product

# (w \/ y) /\ (x -> ¬z) /\ ¬w
print('w x y z')
for w, x, y, z in product((0, 1), repeat=4):
    f = not w or (w == (not y)) and ((not x) <= z)
    if not f:
        print(w, x, y, z)
