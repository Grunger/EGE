from random import choice

s = 'BEDS'
with open('24_1.txt', 'w') as f:
    for _ in range(1000000):
        f.write(choice(s))
