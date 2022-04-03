# Автор: А.А. Фахуртдинова
import time
start_time = time.time()

m = 69
#  минимальная частичная сумма и ее длина для остатка p
ds = [[-1], [-1]] * m
#  максимальная частичная сумма и ее длина для остатка p
ts = [[-1], [-1]] * m
f = open("27-71b.txt")
sw = 0  # Очередная найденная сумма
for i in range(int(f.readline())):
    a = int(f.readline())  # Чтение чисел по одному
    sw += a
    p = sw % m
    if ds[p][0] > 0:
        ts[p] = [sw, i]  # текущая частичная сумма для остатка p
    else:
        ds[p] = [sw, i]  # минимальная частичная сумма для остатка p
        ts[p] = [sw, i]  # начальная максимальная частичная сумма для остатка p
# обработаны все числа, далее анализ найденных частичных сумм
if ds[0][0] > 0:
    smax = [ts[0][0], ts[0][1] + 1]
else:
    smax = [0, 0]
for p in range(1, m):
    if ds[p][0] > 0:
        sw = ts[p][0] - ds[p][0]
        lw = ts[p][1] - ds[p][1]
        if sw > smax[0]:
            smax = [sw, lw]
        elif sw == smax[0]:
            smax = [sw, min(lw, smax[1])]
print(' Ответ -', smax)

f.close()
print('time=', (time.time() - start_time), 'cek')
