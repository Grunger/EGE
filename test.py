from itertools import product


alphabet = '0123456789ABCDEF'

k = 0
for item in product(alphabet, repeat=5):
    if item[4] not in '02468ACE' and item[0] != '1' and item[0] != '0':
        k += 1
print(k)
