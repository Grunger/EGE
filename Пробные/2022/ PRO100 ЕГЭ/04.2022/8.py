from itertools import product


k = 0
for i in product('ГОЛ', repeat=20):
    f = True
    for j in range(19):
        if i[j] == i[j + 1]:
            f = False
            break
    if not f or i[0] == 'Г' or i[-1] == 'Г':
        continue
    for j in range(1, 18):
        if i[j] == 'Г' and i[j - 1] == i[j + 1]:
            f = False
            break
    if not f:
        continue
    k += 1
print(k)
