from random import choice

with open('24-1.txt', mode='w') as f:
    s = 'ABCDE'
    for i in range(100000):
        f.write(choice(s))
    f.write('\n')
