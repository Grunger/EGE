# (¬x ∧ y ∧ z) ∨ (¬x ∧ ¬z)

print('y z x f')
g = (False, True)
for y in g:
    for z in g:
        for x in g:
            f = (not x and y and z) or (not x and not z)
            if f:
                print(int(y), int(z), int(x), int(f))
