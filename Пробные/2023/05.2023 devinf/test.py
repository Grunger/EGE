f = open('26.txt')
k = int(f.readline())
n = int(f.readline())
a = [[int(j) for j in i.split()] for i in f]
a.sort()
cells = [0] * k  # с учетом времени на разгрузку
cells2 = [0] * k  # без учета времени на разгрузку
cnt = 0  # не смогли оставить
cnt2 = 0  # смогли оставить
all_time = 0
for t in range(1441):
    # освобождение
    for i in range(k):
        if cells[i] == t:
            cells[i] = 0
        if cells2[i] == t:
            cells2[i] = 0
    if 0 not in cells2:
        all_time += 1
    # занимаем
    for st, fn in a:
        if st == t:
            if 0 in cells:
                i = cells.index(0)
                cells[i] = t + fn + 1
                cells2[i] = t + fn
                cnt2 += 1
            else:
                cnt += 1

print(cnt, n - cnt2)
print(all_time)

