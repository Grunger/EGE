from random import randint

with open('27A.txt', 'w') as f:
    f.write('10\n')
    for i in range(10):
        x = randint(-100, 100)
        f.write(str(x) + '\n')
