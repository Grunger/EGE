for a in range(1, 1000):
    if all(((x % 2 == 0) <= (x % 3 != 0)) or (x + a >= 100) for x in range(1, 1000)):
        print(a)
        break
