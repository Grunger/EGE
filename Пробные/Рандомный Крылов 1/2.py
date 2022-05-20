a = (False, True)
print('x y z w')
for x in a:
    for y in a:
        for z in a:
            for w in a:
                f = not(z <= w) or x or not y
                if not f:
                    print(*map(int, [x, y, z, w]))
