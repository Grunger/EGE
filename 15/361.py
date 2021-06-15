def f(x):
    return ((x not in a) <= (x < 2 or x > 20)) or (15 <= x <= 25)

a = []
for i in range(1, 1000):
    if not f(i / 10):
        a.append(i / 10)
print(a)
print(a[-1] - a[0])
