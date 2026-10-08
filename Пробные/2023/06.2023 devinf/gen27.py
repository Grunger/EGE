from random import randint

n = 10**6
with open('27_B.txt', 'w') as f:
    f.write(f'{n}\n')
    for i in range(n):
        st = randint(1, 10**8)
        f.write(f'{st}\n')
