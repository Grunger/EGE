from random import randint

with open('26.txt', 'w') as f:
    n = 1000
    m = 100
    f.write(f'{n} {m}\n')
    for _ in range(n):
        x = randint(1, 1000)
        f.write(f'{x}\n')
