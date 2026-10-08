from random import randint

with open('26.txt', 'w') as f:
    n = 2400
    s = 100000
    f.write(f'{n} {s}\n')
    for _ in range(n):
        f.write(f'{randint(20, 100)} {randint(0, 1)}\n')
