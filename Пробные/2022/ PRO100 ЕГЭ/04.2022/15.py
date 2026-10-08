def f():
    return all((680 * y + 256 * x < a) or (5 * x + 3 * y > 11111) for x in range(10000) for y in range(10000))

for a in range(3518040):
    if f():
        print(a)