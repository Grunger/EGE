from random import randint

with open('26_cinema.txt', 'w') as f:
    n = 10000
    f.write(f'{n}\n')
    for i in range(n):
        x = randint(1, 1000)
        y = randint(1, 1000)
        f.write(f'{x} {y}\n')
