from random import choice

with open('24-2.txt', mode='w') as f:
    s = 'SVTLR'
    for i in range(1000000):
        f.write(choice(s))
    f.write('\n')
