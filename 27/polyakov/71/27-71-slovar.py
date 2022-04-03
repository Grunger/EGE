# Автор: А.А. Фахуртдинова
import time
start_time = time.time()

m = 69
ds, ts = {}, {}
ks = [] * m  # Список найденных ключей ( остатков частичных сумм)

f = open("27a.txt")
sw = 0  # Очередная найденная сумма
for i in range(int(f.readline())):
    a = int(f.readline())  # Чтение чисел по одному
    sw += a
    k = sw % m
    if k not in ks:
        ks.append(k)
        ds[k] = [sw, i]  # минимальная частичная сумма с остатком k
        ts[k] = [sw, i]  # начальная максимальная частичная сумма с остатком k
    else:
        ts[k] = [sw, i]  # текущая частичная сумма с остатком k

if 0 in ks:
    ds[0][1] = -1
    ds[0][0] = 0
smax = [0, 0]
for j in ks:
    sw = ts[j][0] - ds[j][0]
    lw = ts[j][1] - ds[j][1]
    if sw > smax[0]:
        smax = [sw, lw]
    elif sw == smax[0]:
        smax = [sw, min(lw, smax[1])]
print(' Ответ -', smax)

f.close()
print('time=', (time.time() - start_time), 'cek')
