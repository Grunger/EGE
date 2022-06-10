from random import randint

with open('26_apple.txt', 'w') as f:
    n = 20000
    f.write(f'{n}\n')
    for i in range(n):
        x = randint(1, 100000)
        y = randint(1, 100000)
        f.write(f'{x} {y}\n')
