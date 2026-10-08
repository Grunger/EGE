
for x in '0123456789abcdefgh':
    a = int(f'451{x}', 18) + int(f'79{x}2', 18)
    if a % 27 == 0:
        print(a // 27)
