from itertools import product


k = 0
p = 0
for item in product('АГИЛМОРТ', repeat=5):
    p += 1
    if (p % 2 == 0 and
            item[0] != 'М' and
            item.count('А') + item.count('И') + item.count('О') <= 2):
        k += 1
print(k)


k = 0
p = 0
for item in product('АГИЛМОРТ', repeat=5):
    p += 1
    if (p % 2 == 1 and
            item[0] != 'О' and
            item.count('Т') + item.count('Г') + item.count('Л') + item.count('М') + item.count('Р') >= 2):
        k += 1
print(k)
