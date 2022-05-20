from itertools import permutations

# x ∧ (y → z) ∨ w
# 1 0 x 1 0
# x 0 1 0 0
# x 0 x x 0


def f(x, y, z, w):
    return bool(x) and (y <= z) or bool(w)


x = True
y = x
z = x
w = x
d = {'x': x,
     'y': y,
     'z': z,
     'w': w}
p = 'xyzw'

# 1 0 x 1 0
ways = set()
for i in permutations(p):
    for n in (0, 1):
        d[i[0]], d[i[1]], d[i[2]], d[i[3]] = 1, 0, n, 0
        print(d['x'], d['y'], d['z'], d['w'])
        print(f(d['x'], d['y'], d['z'], d['w']))
        if not f(d['x'], d['y'], d['z'], d['w']):
            ways.add(i)
# x 0 1 0 0
ways1 = set()
for i in ways:
    k = 0
    for n in (1, 0):
        d[i[0]], d[i[1]], d[i[2]], d[i[3]] = n, 0, 1, 0
        if not f(d['x'], d['y'], d['z'], d['w']):
            k += 1
    if k:
        ways1.add(i)
# x 0 x x 0
ways2 = set()
for i in ways1:
    k = 0
    for n in (1, 0):
        for m in (1, 0):
            for b in (1, 0):
                d[i[0]], d[i[1]], d[i[2]], d[i[3]] = n, 0, m, b
                if not f(d['x'], d['y'], d['z'], d['w']):
                    k += 1
    if k:
        ways2.add(i)

print(ways2)
