from random import randint, choice

with open('26_apple.txt', 'w') as f:
    n = 20000
    f.write(f'{n}\n')
    d = set()
    while len(d) < 1000:
        d.add(randint(1, 10000))
    for i in range(n):
        x = choice(list(d))
        y = randint(1, 10000)
        f.write(f'{x} {y}\n')
