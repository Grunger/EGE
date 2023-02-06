from random import randint

with open('27-B.txt', 'w') as f:
    n = 2024000
    f.write(f'{n}\n')
    for _ in range(n):
        x = randint(1, 100)
        f.write(f'{x}\n')
