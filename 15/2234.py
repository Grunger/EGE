def dell(n, m):
    return n % m == 0


def f(x, a):
    return (not dell(x, a)) <= (dell(x, 10) <= (not dell(x, 12)))


for a in range(1, 5000000):
    if all(f(x, a) for x in range(1, 10000)):
        print(a)
