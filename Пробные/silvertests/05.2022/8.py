from itertools import product

s = 'АВЕНС'
for k, i in enumerate(product(s, repeat=6), start=1):
    if set(s) == set(i) and all(i[j] != i[j + 1] for j in range(5)):
        print(k)
