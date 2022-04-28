from random import randint

with open('17-04-1.txt', 'w') as f:
    for _ in range(3210):
        f.write(str(randint(1, 1000)) + '\n')
