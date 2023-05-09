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
for t in range(1441):
    # print(t, cells)
    # освобождаем
    for i in range(k):
        if cells[i] == t:
            cells[i] = 0
    for i in range(k):
        if cells2[i] == t:
            cells2[i] = 0
    if 0 not in cells2:
        count_t += 1
        # print(t)
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
print(count, n - cnt)
# 512
print(count_t)
# 617
