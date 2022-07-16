from random import randint

with open('26_adv.txt', 'w') as f:
    n = 10000
    f.write(f'{n}\n')
    for i in range(n):
        x = randint(0, 10000)
        y = randint(5000, 15000)
        f.write(f'{x} {y}\n')
