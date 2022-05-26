for a in range(1000):
    if all((x & 83) != 3 or ((x & 44 == 8) <= (x & a == 0)) for x in range(1000)):
        print(a)
