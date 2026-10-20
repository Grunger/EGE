# https://openfipi.devinf.ru/task/A4B351
f = open('83B7FD.txt')
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
    id, v = a[t]
    c[id] += v
mx = [i for i in c if i >= 150_000]
mx.sort()
print(sum(mx[:2]))
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
mx = [[i, j] for i, j in mx if j < 12*3600]
print(min(mx)[0])
