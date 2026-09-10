f = open('24-06.txt')
s = f.read().strip()
pr = []
pa = []
for i in range(len(s)):
    if s[i] == 'R':
        pr.append(i)
    if s[i] == 'A':
        pa.append(i)

m = 0  # максимум
a = [0, pa[4] - 1]  # берем подстроку с 3 А
cnt = 0
while a[-1] != pa[-1] - 1:  # пока не перебрали все подстроки
    k = 0  # считаем сколько R
    for i in range(a[0], a[1] + 1):
        if i in pr:
            k += 1
    if k >= 2:
        m = max(m, a[1] - a[0])
    cnt += 1
    a[0] = pa[cnt]
    a[1] = pa[cnt + 4] - 1
# последняя подстрока
a[0] = a[1]
a[1] = len(s)
k = 0
for i in range(a[0], a[1] + 1):
    if i in pr:
        k += 1
if k >= 2:
    m = max(m, a[1] - a[0])
print(m)
