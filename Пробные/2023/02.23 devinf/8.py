from itertools import product

for n, i in enumerate(product('ЕКОФ', repeat=5), start=1):
    if i.count('О') == 1 and all(j not in ''.join(i) for j in ('ОК', 'КО', 'ОФ', 'ФО')):
        print(n, i)
