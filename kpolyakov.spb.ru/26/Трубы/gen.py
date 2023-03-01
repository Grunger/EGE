from random import randint

with open('26.txt', 'w') as f:
    n = 1000
    m = 120
    f.write(f'{n} {m}\n')
    for _ in range(n):
        x = randint(1, 2000)
        f.write(f'{x}\n')
