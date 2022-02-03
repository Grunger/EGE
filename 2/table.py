from itertools import product


# (w \/ y) /\ (x -> ¬z) /\ ¬w
print('w x y z f')
for w, x, y, z in product((0, 1), repeat=4):
    f = (w or y) and (x <= (not z)) and not w
    if f:
        print(w, x, y, z, f)
