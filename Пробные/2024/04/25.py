from fnmatch import fnmatch

ans = []
x1, x2, x3 = 2023, 2147, 2193
mask = '157*4?24'
print('-' * 100)
for i in range(0, 10**10, x1):
    if i % x2 != 0 and i % x3 != 0 and fnmatch(str(i), mask):
        print(i, i // x1)
print('-' * 100)
for i in range(0, 10**10, x2):
    if i % x1 != 0 and i % x3 != 0 and fnmatch(str(i), mask):
        print(i, i // x2)
print('-' * 100)
for i in range(0, 10**10, x3):
    if i % x2 != 0 and i % x1 != 0 and fnmatch(str(i), mask):
        print(i, i // x3)
print('-' * 100)
for i in range(0, 10**10):
    if ((i % x1 == 0) + (i % x2 == 0) + (i % x3 == 0) >= 2) and fnmatch(str(i), mask):
        print(i)