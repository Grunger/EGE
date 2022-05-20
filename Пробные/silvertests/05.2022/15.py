for a in range(10000):
    if all(((x - a < 5) and (x + a >= 85)) or ((x % 7 == 0) <= (x % 9 == 0)) for x in range(1000)):
        print(a)