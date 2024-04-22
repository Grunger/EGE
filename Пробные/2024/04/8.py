from itertools import product

k = 0
p = 0
for item in product('АГИЛМОР', repeat=5):
    p += 1
    if p % 2 == 1 and item[0] != 'О' and item.count('Г') + item.count('Л') + item.count('М') + item.count('Р') >= 2:
        k += 1
print(k)
