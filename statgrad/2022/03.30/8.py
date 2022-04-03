from itertools import product


k = 0
for i in product('НАСТЯ', repeat=7):
    if i.count('Н') == 2 and i.count('А') >= 1:
        k += 1
print(k)
