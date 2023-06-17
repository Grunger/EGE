from random import randint

n_a = 100
n_b = 10**6 * 3

with open('../27/devinf/Пары/03/27_A.txt', 'w') as f:
    f.write(f'{n_a}\n')
    for _ in range(n_a):
        f.write(f'{randint(1, 1000)}\n')

with open('../27/devinf/Пары/03/27_B.txt', 'w') as f:
    f.write(f'{n_b}\n')
    for _ in range(n_b):
        f.write(f'{randint(1, 1000)}\n')
