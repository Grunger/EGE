from random import randint

with open('27_B.txt', 'w') as f:
    f.write('10000000' + '\n')
    for _ in range(10000000):
        f.write(str(randint(1, 2000)) + '\n')
