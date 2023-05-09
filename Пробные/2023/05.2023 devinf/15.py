for a in range(0, 1000):
    if all((2 * x + y != 150) or not (50 <= x <= 70) or (a > y) for x in range(1000) for y in range(1000)):
        print(a)
