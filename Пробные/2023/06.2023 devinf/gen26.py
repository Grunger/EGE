from random import randint

k = 500
n = 3200
gens = set()
with open('26.txt', 'w') as f:
    f.write(f'{k}\n')
    f.write(f'{n}\n')
    for i in range(n):
        st = randint(1, 86000)
        while st in gens:
            st = randint(1, 86000)
        gens.add(st)
        t = randint(st + 1, 86400)
        f.write(f'{st} {t}\n')
