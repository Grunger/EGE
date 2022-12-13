from random import choice


s = 'DEVINF'

with open('24_3.txt','w') as f:
    for _ in range(1_000_000):
        f.write(choice(s))
    f.write('\n')
