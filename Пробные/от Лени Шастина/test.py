f = open('26.txt')
n = int(f.readline())
d = dict()  # ключ - время, значение - сколько заказов готово
orders = set()  # ключ - номер заказа, значение - готов или нет

data = []
for _ in range(n):
    t, x = map(int, f.readline().split())
    data.append([t, x])

for order in sorted(data, key=lambda x: x[0]):
    t, x = order
    # заказ готов
    if x in orders:
        d[t] = d.get(t, 0) + 1
        orders.remove(x)
    else:
        orders.add(x)
m = 0
for time in range(1000):
    order = [d[i] for i in d if time <= i <= time + 59]
    m = max(m, sum(order))
print(m)

d = dict()  # ключ - номер заказа, значение - список из времени готовки
orders = dict()  # ключ - номер заказа, значение - готов или нет
for t, x in sorted(data):
    # заказ готов
    if x in orders and orders[x] != -1:
        new = d.get(x, [])
        new.append(t - orders[x])
        d[x] = new
        orders[x] = -1
    else:
        orders[x] = t
for i in d:
    d[i] = sum(d[i]) / len(d[i])
print(max(d, key=lambda x: d[x]))
