from itertools import product

k = 0
for item in product('ПРОЛИВ', repeat=6):
    if item.count('П') >= 1:
        k += 1
print(k)
