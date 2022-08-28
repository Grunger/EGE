# Автор: А. Кабанов

f = open('27_B.txt')
n, v = int(f.readline()), 36
a = []
for i in range(n):
    s, k = map(int, f.readline().split())
    # кол-во сумок
    c = k // v if k % v == 0 else k // v + 1
    a.append([s, c])
a.sort()

# решение В
# префиксные суммы количества сумок в первых п пунктах
bags = [0] * n
bags[0] = a[0][1]
for i in range(1, n):
    bags[i] = bags[i - 1] + a[i][1]
# считаю стоимость доставки в нулевом пункте
s = 0
for j in range(n):
    s += abs(a[0][0] - a[j][0]) * a[j][1]

ms = s
for i in range(1, n):
    # расстояние между двумя пунктами
    diff = a[i][0] - a[i - 1][0]
    # для предыдущих пунктов дороже, для следующих дешевле
    s = s + diff * bags[i - 1] - diff * (bags[n - 1] - bags[i - 1])
    ms = min(ms, s)

print(ms)
