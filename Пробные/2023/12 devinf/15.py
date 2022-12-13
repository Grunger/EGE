for a in range(1000):
    f = lambda x, y: not((x + 5 < a) <= (y > a)) or x * y >= 76
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
