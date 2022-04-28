def f():
    return all((2 * x + y != 100) or (x <= y) or (a <= x) for x in range(1000) for y in range(1000))


for a in range(1000):
    if f():
        print(a)
