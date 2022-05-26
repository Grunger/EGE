from string import ascii_uppercase
from random import choice, randint


with open('26.txt', 'w') as f:
    coords = set()
    while len(coords) < 6000:
        row = randint(1, 1000)
        col = choice(ascii_uppercase)
        coords.add((col, row))
    f.write('6000\n')
    for col, row in coords:
        f.write(col + ' ' + str(row) + '\n')
