# ((a ∧ b) ≡ ¬c) ∧ (b → d)
# 1 0 0 0 1
# 1 0 1 0 1
# 1 0 1 1 1
# 1 1 0 0 1
print('c a d b')
g = (False, True)
for a in g:
    for b in g:
        for c in g:
            for d in g:
                f = ((a and b) == (not c)) and (b <= d)
                if f:
                    print(int(c), int(a), int(d), int(b))

