f = open('26.txt')
n = int(f.readline())
d = dict()  # ключ - время, значение - сколько заказов готово
orders = dict()  # ключ - номер заказа, значение - готов или нет

data = []
for _ in range(n):
    t, x = map(int, f.readline().split())
    data.append([t, x])

for order in sorted(data):
    t, x = order
    # заказ готов
    if orders.get(x, False):
        d[t] = d.get(t, 0) + 1
        orders.pop(x)
    else:
        orders[x] = x in orders
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
        if x in orders:
            orders[x] = t
        else:
            orders[x] = -1
for i in d:
    d[i] = sum(d[i]) / len(d[i])
print(max(d, key=lambda x: d[x]))
