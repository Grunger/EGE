from itertools import product


# (w \/ y) /\ (x -> ¬z) /\ ¬w
print('w x y z f')
for w, x, y, z in product((0, 1), repeat=4):
    f = not w and (w == (not y)) and ((not x) <= z)
    if f:
        print(w, x, y, z, f)
