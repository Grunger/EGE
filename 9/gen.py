from random import randint, shuffle

with open('9.csv', 'w') as f:
    for _ in range(6200):
        p = randint(1, 100)
        if p > 60:
            x = [randint(1, 100) for i in range(2)] * 3 + [randint(1, 100)]
        else:
            x = [randint(1, 100) for i in range(7)]
        shuffle(x)
        f.write(';'.join(map(str, x)) + '\n')
