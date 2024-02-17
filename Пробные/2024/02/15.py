def f(a):
    return all((x + y < a) or (2 * y > x) or (x > 90) for x in range(1000) for y in range(1000))


for a in range(1000):
    if f(a):
        print(a)
        break
