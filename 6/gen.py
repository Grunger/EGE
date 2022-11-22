from random import random, randint

with open('6.txt', 'w') as f:
    for _ in range(1000):
        f.write(f'{randint(-5, 5) + random():2.1f} {randint(-5, 5) + random():2.1f}\n')
