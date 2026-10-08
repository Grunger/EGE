from random import randint

with open('17-1.txt', 'w') as f:
    for _ in range(3500):
        f.write(str(randint(-1000, 1000)) + '\n')
