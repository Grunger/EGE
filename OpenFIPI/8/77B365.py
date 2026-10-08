from itertools import product

k = 1
for item in product('ЕЛМРУ', repeat=4):
    if item[0] == 'У':
        print(k)
        break
    k += 1
