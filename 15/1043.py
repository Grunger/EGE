def f(x, y, a):
    return (3 * x + 2 * y != 90) or ((a > x) and (a > y))


for a in range(1, 1000):
    if all(f(x, y, a) for x in range(1000) for y in range(1000)):
        print(a)
