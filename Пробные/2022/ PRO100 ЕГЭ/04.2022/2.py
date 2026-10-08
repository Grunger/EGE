from itertools import product


print('c a d b')
for a, b, c, d in product((0, 1), repeat=4):
    f = ((a and b) == (not c)) and (b <= d)
    if f and c:
        print(c, a, d, b)