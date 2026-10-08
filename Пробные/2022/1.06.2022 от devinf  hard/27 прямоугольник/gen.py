from random import randint

with open('27A.txt', 'w') as f:
    f.write('20 20\n')
    f.write('100\n')
    for i in range(100):
        x = randint(0, 20)
        y = randint(0, 20)
        f.write(f'{x} {y}\n')
