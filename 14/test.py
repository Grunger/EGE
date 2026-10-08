from func import to_base

x = 14 * 256 ** 19 - 25 * 64 ** 16 + 2 * 16 ** 11 - 33
x = to_base(x, 10, 4)
print(x.count('3'))
