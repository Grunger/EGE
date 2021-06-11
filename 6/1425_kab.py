def f(s):
    n = 1
    while s < 94:
        s += 8
        n *= 2
    return n


for s in range(1000):
    if f(s) == 32:
        print(s)
