for a in range(1, 1000):
    if all(((x % 3 == 0) <= (x % 5 != 0)) or (x + a >= 90) for x in range(1, 1000)):
        print(a)
        break