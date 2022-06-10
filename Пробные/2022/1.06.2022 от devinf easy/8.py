from itertools import product

s = 'ЛЕГКО'
k = 0
for i in product(s, repeat=6):
    if i.count('О') <= 1 and i[0] != 'Г' and i[-1] not in 'ЕО':
        k += 1
print(k)
