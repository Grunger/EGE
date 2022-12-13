from itertools import product

k = 0
for item in product('АРБУЗ', repeat=6):
    if item.count('А') == 3 and 'АА' in ''.join(item) and 'ААА' not in ''.join(item):
        k += 1
print(k)

print(4**3 * 3 * 2 + 4**3 * 2 * 3)
