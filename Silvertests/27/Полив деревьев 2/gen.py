from random import randint

with open('27C.txt', 'w') as f:
    n = 1
    f.write(f'{n}\n')
    for i in range(n):
        x = randint(0, 10)
        f.write(f'{x}\n')
