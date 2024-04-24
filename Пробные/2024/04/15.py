def f(x, a):
    return ((x % a != 0) and (x % 56 == 0)) <= ((x % 22 != 0) or (x % 56 != 0))


for a in range(1, 500):
    if all(f(x, a) for x in range(1, 1000)):
        print(a)
