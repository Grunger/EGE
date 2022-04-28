from itertools import product


# (x \/ -y) /\ (x -> ¬z) /\ ¬w
print('w x y z f')
for w, x, y, z in product((0, 1), repeat=4):
    f = not w and (x == (not y)) and ((not x) <= z)
    if f:
        print(w, x, y, z, f)
