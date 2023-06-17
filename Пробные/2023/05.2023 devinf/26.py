f = open('26.txt')
k = int(f.readline())
n = int(f.readline())
a = [[int(i) for i in j.split()] for j in f]
a.sort()
cells = [0] * k
cells2 = [0] * k
count = 0
cnt = 0
count_t = 0
count_t2 = 0
for t in range(1441):
    # print(t, cells)
    # освобождаем
    for i in range(k):
        if cells[i] == t:
            cells[i] = 0
    for i in range(k):
        if cells2[i] == t:
            cells2[i] = 0
    # Проверяем, все ли ячейки заняты по версии 1
    if 0 not in cells2:
        count_t2 += 1
    # занимаем
    for st, time in a:
        if st == t:
            if 0 in cells:
                for i in range(k):
                    if cells[i] == 0:
                        cells[i] = st + time + 1
                        cells2[i] = st + time
                        cnt += 1
                        break
            else:
                count += 1
    # Проверяем, все ли ячейки заняты по версии 2
    if 0 not in cells2:
        count_t += 1
print(count, n - cnt)
print(count_t)
print(count_t2)

