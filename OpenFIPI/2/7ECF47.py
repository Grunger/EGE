from itertools import permutations

def f(x, y, z, w):
    return x and not y and (not z or w)

t = [
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [1, 0, 1, 1]
]
s = 'xyzw'
for p in permutations(s):
    p1, p2, p3, p4 = p
    p1 = s.index(p1)
    p2 = s.index(p2)
    p3 = s.index(p3)
    p4 = s.index(p4)
    fl = True
    for st in t:
        if not f(st[p1], st[p2], st[p3], st[p4]):
            fl = False
    if fl:
        print(p)

