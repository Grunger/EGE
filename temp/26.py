f = open('26-00_6071.txt')
n = int(f.readline())

cost = []
for line in f:
    id, st1, st2 = map(int, line.split())
    cost.append([id, st1, st2])
goods = {i[0] for i in cost}

d = dict()
for item in cost:
    id, st1, st2 = item
    if id - 10 in goods and id - 10 not in d:
        d[id - 10] = st1
    if id + 10 in goods and id + 10 not in d:
        d[id + 10] = st2

cart = [sorted(d.values())[0]]
m = 0
for item in sorted(d.values()):
    if item - cart[-1] >= 50 + len(cart) + 1:
        cart.append(item)
    elif m == 0:
        m = item
print(len(cart))
print(cart)
print(m)