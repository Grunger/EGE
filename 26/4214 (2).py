# Организация купила для своих сотрудников все места в нескольких подряд идущих рядах на концертной площадке.
# Известно, какие места уже распределены между сотрудниками.
# Найдите ряд с наибольшим номером, в котором есть два соседних места,
# таких что слева и справа от них в том же ряду места уже распределены (заняты).
# Гарантируется, что есть хотя бы один ряд, удовлетворяющий условию.
# Входные данные представлены в файле 26-59.txt следующим образом.
# В первой строке входного файла находится одно число: N – количество занятых мест
# (натуральное число, не превышающее 10 000). В следующих N строках находятся пары чисел:
# ряд и место выкупленного билета, не превышающие 10000. В ответе запишите два целых числа:
# номер ряда и наименьший номер места из найденных в этом ряду подходящих пар.

f = open('26-59.txt')

n = int(f.readline())
pos = {}
for i in range(n):
    x, y = map(int, f.readline().split())
    pos[x] = pos.get(x, []) + [y]
print('Read done')
stop = False
for x in sorted(pos.keys(), reverse=True):
    for y in sorted(pos[x]):
        if any(abs(y - z) == 3 for z in pos[x]):
            print(x, y + 1)
            stop = True
            break
    if stop:
        break
