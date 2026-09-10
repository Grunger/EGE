from itertools import product

s = sorted('ЭКЗАМЕН')
k = 0
for i in product(s, repeat=6):
    i = ''.join(i)
    k += 1
    if k % 2 != 0:
        if i[0] not in 'АЗ':
            if i.count('Н') >= 2:
                print(k, i)
                break
