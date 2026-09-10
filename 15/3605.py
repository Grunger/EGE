def dell(n, m):
    return n % m == 0


def f(x, a):
    return (not dell(x, 84) or not dell(x, 90)) <= (not dell(x, a))


for a in range(1, 10000):
    if all(f(x, a) for x in range(1, 10000)):
        print(a)
        break
