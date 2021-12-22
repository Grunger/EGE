from pprint import pprint

f = open('files/71/27-71.txt')
n = int(f.readline())

m = 0
l = 0
# все суммы по остаткам от деления
sums = {i: 0 for i in range(69)}
# соответствующие суммам начала
start = {i: 0 for i in range(69)}
for i in range(n):
    x = int(f.readline())
    new_sums = {}
    for j in sums:
        s = x + sums[j]
        ost = (x + sums[j]) % 69
        if s > sums[ost]:
            pass
print(m, l)

# 2 14 99989
# 47955
