from random import randint, choice

f = open('26-05.txt', 'w')
f.write('5000\n')
s = [i for i in range(1, 50, 2)]
for i in range(5000):
    row = randint(1, 10000)
    col = randint(1, 10000)
    size = choice(s)
    f.write(f'{row} {col} {size}\n')
f.close()
