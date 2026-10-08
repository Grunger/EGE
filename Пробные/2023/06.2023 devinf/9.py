f = open('9.csv').read().split()
k = 0
for line in f:
    item = [int(i) for i in line.split(';')]
    item.sort()
    if len(set(item)) == 4 and (item[0] + item[4]) ** 2 < item[1] ** 2 + item[2] ** 2 + item[3] ** 2:
        k += 1
print(k)
