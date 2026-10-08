def dell(n, m):
    return n % m == 0


for a in range(1, 100000):
    if all((not dell(x, a)) <= (dell(x, 26) <= (not dell(x, 169))) for x in range(1, 100000)):
        print(a)
