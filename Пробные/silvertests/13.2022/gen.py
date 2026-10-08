from random import randint

with open('27.txt', 'w') as f:
    f.write('4000000' + '\n')
    for i in range(4000000):
        f.write(str(randint(1, 2000)) + '\n')
