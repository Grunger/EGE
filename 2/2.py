# (¬z) ∧ x ∨ x ∧ y

print('z y x f')
g = (False, True)
for w in g:
    for z in g:
        for y in g:
            for x in g:
                f = w and (z == (not x)) or ((not x) or y) or not x
                if not f:
                    print(int(x), int(y), int(z), int(w))
