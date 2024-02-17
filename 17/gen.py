from random import randint

with open('17.txt', 'w') as f:
    n = 6536
    for i in range(n):
        x = randint(1, 100001)
        f.write(f'{x}\n')
