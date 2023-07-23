from itertools import product

k = 0
for item in product(range(9), repeat=5):
    x = ''.join([str(i) for i in item])
    if item[0] != 0 and item.count(3) == 1 and all(j not in x for j in ('53', '63', '73', '83', '35', '36', '37', '38')):
        k += 1
print(k)
