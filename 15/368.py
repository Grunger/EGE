def f(x):
    return ((x in a) <= (x in p)) or ((x not in q) <= (x not in a))


p = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
q = {i for i in range(5, 51, 5)}
a = {i for i in range(1, 1000)}
for i in range(1, 1000):
    if not f(i):
        a.remove(i)
print(len(a))

for i in range(1, 1000):
    if not f(i):
        print(i)
