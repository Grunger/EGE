from itertools import product


a = 'ЕЗКНУЦ'
for i, s in enumerate(product(a, repeat=6), start=1):
    print(i, ''.join(s))
    if ''.join(s) == 'КУЗНЕЦ':
        break
