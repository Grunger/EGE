from random import randint

with open('26_store.txt', 'w') as f:
    f.write('50000\n')
    for i in range(10000):
        x = randint(0, 10000)
        y = randint(5000, 15000)
        if x > y:
            x, y = y, x
        f.write(f'{x} {y}\n')
    for i in range(10000):
        x = randint(20000, 24000)
        y = randint(25000, 30000)
        if x > y:
            x, y = y, x
        f.write(f'{x} {y}\n')
    for i in range(10000):
        x = randint(32451, 41237)
        y = randint(35124, 42347)
        if x > y:
            x, y = y, x
        f.write(f'{x} {y}\n')
    for i in range(10000):
        x = randint(43124, 47145)
        y = randint(44786, 48124)
        if x > y:
            x, y = y, x
        f.write(f'{x} {y}\n')
    for i in range(10000):
        x = randint(64123, 69145)
        y = randint(68142, 86399)
        if x > y:
            x, y = y, x
        f.write(f'{x} {y}\n')
