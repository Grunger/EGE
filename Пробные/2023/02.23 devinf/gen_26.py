from random import randint

s = 'XYZ'
with open('24.txt', 'w') as f:
    for _ in range(1000000):
        x = randint(0, 2)
        f.write(s[x])
