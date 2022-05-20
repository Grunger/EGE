# a ∧ ¬b ∨ (a ∨ b) ∧ c ∨ d
# x x x 1 0
# x 1 x 1 0
# 1 x x x 0

print('c a d b')
g = (False, True)
for a in g:
    for b in g:
        for c in g:
            for d in g:
                f = a and not b or (a or b) and c or d
                if not f:
                    print(int(c), int(a), int(d), int(b))

