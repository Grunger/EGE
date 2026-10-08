def f(x, y):
    return (2 * x + y != 300000) or (x < y) or (a < x)


for a in range(3*10**5, 0, -1):
    print(a)
    if all(f(x, y) for x in range(3*10**5) for y in range(3*10**5)):
        print(a)
        break
    