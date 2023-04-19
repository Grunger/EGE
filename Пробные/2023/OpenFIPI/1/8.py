from itertools import product


k = 0
for x in product('012345', repeat=6):
    x = ''.join(x)
    if x[0] != '0' and x.count('2') == 1 and all(n not in x for n in ('12', '32', '52', '21', '23', '25')):
        k += 1
print(k)
