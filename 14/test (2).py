from func import to_base

x = 81 ** 820 - 9 ** 761 - 3 ** 2022 + 14
x = to_base(x, 10, 9)
print(x.count('8'))
