from random import randint

with open('26_books.txt', 'w') as f:
    n = 3000
    f.write(f'{n} 30000\n')
    for i in range(n):
        x = randint(10, 800)
        y = randint(0, 1)
        f.write(f'{x} {y}\n')
