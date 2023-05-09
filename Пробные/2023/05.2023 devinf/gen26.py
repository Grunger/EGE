from random import randint

k = 120
n = 989
with open('26.txt', 'w') as f:
    f.write(f'{k}\n')
    f.write(f'{n}\n')
    for i in range(n):
        st = randint(1, 1340)
        t = randint(1, 1340 - st)
        f.write(f'{st} {t}\n')
