# Сколько существует шестеричных пятизначных чисел,
# содержащих в своей записи ровно одну цифру 3,
# в которых никакие две одинаковые цифры не стоят рядом?

from itertools import product

a = '0123'
k = 0
for i in product(a, repeat=5):
    s = ''.join(i)
    if s.count('3') == 1 and s[0] != '0' and all(c + c not in s for c in a):
        k += 1

print(k)
