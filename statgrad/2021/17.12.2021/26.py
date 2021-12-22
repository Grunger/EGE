f = open('26.txt')
n = int(f.readline())
d = dict()
print(n)
start = 1633305600
end = 1633305600 + 7 * 24 * 60 * 60  # 1633910400
# Словарь хранит изменение количества запущенных
# процессов по участвующим моментам времени
while x := f.readline():
    x = list(map(int, x.split()))
    if x[0] < start:
        x[0] = start - 1
    if x[1] == 0 or x[1] > end:
        x[1] = end + 1
    d[x[0]] = d.get(x[0], 0) + 1
    d[x[1]] = d.get(x[1], 0) - 1
# Для известных участков считаем количество запущенных процессов
run = 0
d2 = sorted(d.keys())
m = -n
for i in d2:
    run += d[i]
    if start <= i <= end:
        if run >= m:
            m = run
# Считаем расстояние между точками где количество
# процессов равно максимальному
run = 0
k = 0
for i in d2:
    run += d[i]
    if start <= i <= end:
        if run == m:
            k += d2[d2.index(i) + 1] - i
print(m, k)
