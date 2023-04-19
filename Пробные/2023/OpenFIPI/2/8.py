from itertools import product

k = 0
for i in product('012345', repeat=6):
    i = ''.join(i)
    if i[0] != '0' and i.count('2') == 1 and all(j not in i for j in ('12', '32', '52', '21', '31', '52')):
        k += 1
print(k)
