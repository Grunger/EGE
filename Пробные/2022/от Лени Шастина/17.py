with open('../Пробные/от Лени Шастина/17-1.txt') as f:
    data = [int(i) for i in f.readlines()]
    k = 0
    s = 0
    for i in range(len(data) - 2):
        t = sorted([data[i], data[i + 1], data[i + 2]])
        if t[0] ** 2 + t[1] ** 2 == t[2] ** 2:
            k += 1
            s += t[2]
print(k, s)
