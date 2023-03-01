from random import randint

with open('26.txt', 'w') as f:
    n = 2000
    m = 80
    f.write(f'{n} {m}\n')
    for _ in range(n):
        x = randint(1, 1000)
        f.write(f'{x}\n')
