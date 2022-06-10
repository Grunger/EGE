from itertools import product

s = '01234567'
k = 0
for i in product(s, repeat=6):
    if i[0] != '0' and\
        len(set(i)) == len(i) and\
        int(''.join(i), 8) % 5 == 0:
        if all(int(a) % 2 != int(b) % 2 for a, b in zip(i, i[1:])):
            k += 1
print(k)
