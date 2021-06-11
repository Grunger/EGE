# (¬z) ∧ x ∨ x ∧ y

print('z y x f')
g = (False, True)
for z in g:
    for y in g:
        for x in g:
            f = not z and x or x and y
            print(int(x), int(y), int(z), int(f))
