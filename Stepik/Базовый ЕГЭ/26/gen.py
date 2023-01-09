from random import randint

with open('26_01.txt', 'w') as f:
    s = 10800
    n = 720
    f.write(f'{s} {n}\n')
    for _ in range(n):
        if randint(1, 100) < 90:
            f.write(str(randint(1, 40)) + '\n')
        else:
            f.write(str(randint(70, 90)) + '\n')
