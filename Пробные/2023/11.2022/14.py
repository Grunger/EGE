s = 0
for x in '0123456789abcdefg':
    a = int(f'149{x}3', 17) + int(f'{x}612', 17) - int(f'{x}54{x}', 17)
    if a % 7 == 0:
        s += int(x, 17)
print(s)
