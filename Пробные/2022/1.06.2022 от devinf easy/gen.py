from random import randint

with open('27B.txt', 'w') as f:
    for i in range(200000):
        x = randint(1, 200000)
        f.write(str(x) + '\n')
