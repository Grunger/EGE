# ¬(z ∧ ¬w) ∨ ((z → w) ≡ (x → y))

print('z x w y')
g = (False, True)
for z in g:
    for y in g:
        for x in g:
            for w in g:
                f = not (z and not w) or ((z <= w) == (x <= y))
                if not f:
                    print(int(z), int(x), int(w), int(y))
