for a in range(100):
    if all(((x | 42 > 64) and (x | 34 <= 102)) <= (x | a >= 70) for x in range(1000)):
        print(a)