for a in range(5470, 6000):
    if all((x * y > a) or (x > y) or (74 > x) for x in range(10000) for y in range(10000)):
        print(a)
    else:
        print(a, '----')
