from math import ceil

f = open('27_B.txt')
n = int(f.readline())
# d = dict()
# for line in f:
#     p, k = map(int, line.split())
#     k = ceil(k / 44)
#     d[p] = k
# min_cost = 10 ** 9
# for p1 in d:
#     cost = 0
#     for p2 in d:
#         cost += d[p2] * abs(p2 - p1)
#     min_cost = min(min_cost, cost)
# print(min_cost)

# 55261
v = 44
a = []
for i in range(n):
  s, k = map(int, f.readline().split())
  # кол-во сумок
  c = k//v if k % v == 0 else k//v + 1
  a.append( [s, c] )
a.sort()

# решение В
# префиксные суммы количества сумок в первых п пунктах
bags = [0]*n
bags[0] = a[0][1]
for i in range(1,n):
  bags[i] = bags[i-1] + a[i][1]
# считаю стоимость доставки в нулевом пункте
s = 0
for j in range(n):
  s += abs(a[0][0]-a[j][0])*a[j][1]

ms = s
for i in range(1,n):
  # расстояние между двумя пунктами
  diff = a[i][0] - a[i-1][0]
  # для предыдущих пунктов дороже, для следующих дешевле
  s = s + diff*bags[i-1] - diff*(bags[n-1]-bags[i-1])
  ms = min(ms,s)

print(ms)