def f(x, a):
    return (x & 25 != 0) <= ((x & 17 == 0) <= (x & a != 0))


for a in range(1000):
    if all(f(x, a) for x in range(1000)):
        print(a)
        break
