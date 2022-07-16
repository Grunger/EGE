from random import randint

# with open('26_books.txt', 'w') as f:
#     n = 3000
#     f.write(f'{n} 30000\n')
#     for i in range(n):
#         x = randint(10, 800)
#         f.write(f'{x}\n')

with open('26_books_test.txt', 'w') as f:
    n = 5
    f.write(f'{n} 50\n')
    for i in range(n):
        x = randint(10, 25)
        f.write(f'{x}\n')