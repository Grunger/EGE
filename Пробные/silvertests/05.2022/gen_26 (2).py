from random import randint, choice

f = open('26-05.txt', 'w')
f.write('10000\n')
mx = 1000
s = [i for i in range(1, 50, 2)]
for i in range(10000):
    row = randint(1, mx)
    col = randint(1, mx)
    size = choice(s)
    while row + size // 2 > mx or \
            row - size // 2 < 1 or \
            col + size // 2 > mx or \
            col - size // 2 < 1:
        size = choice(s)
    f.write(f'{row} {col} {size}\n')
f.close()
