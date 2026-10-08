print('x y z w f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (w == (not x)) and (not x or y) and z
                if f:
                    print(x, y, z, w)