def f(x, a):
    return (x & a != 0) <= ((x & 20 == 0) <= (x & 5 != 0))


for a in range(1000):
    if all(f(x, a) for x in range(1000)):
        print(a)
