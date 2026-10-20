# https://openfipi.devinf.ru/task/A4B351
f = open('09681e.txt')
n, k = map(int, f.readline().split())
a = dict()
for line in f:
    t, id, v = line.split()
    id, v = int(id), int(v)
    h, m, s = t.split(':')
    t = int(h) * 3600 + int(m) * 60 + int(s)
    if t not in a:
        a[t] = dict()
    a[t] = (id, v)
# суммарный объем по клиентам
c = [0] * 1_000_000
for t in a:
    if t < 12*3600:
        id, v = a[t]
        c[id] += v
mx = max(c)
# print(mx)
# поиск id клиента
for i in range(1_000_000):
    if c[i] == mx:
        print(i)
# моделируем наполнение
d = 0
mx = []
for t in sorted(a):
    id, v = a[t]
    if d + v <= k:
        d += v
    else:
        mx.append([d, t])
        d = v

print(sorted(mx)[-2:])
print(23218 + 23218)