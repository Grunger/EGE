x = (2 * int('10', 8)) ** 2020 - 4 ** 1111 + 2**2024

print(bin(x).count('1'))
print(bin(x).count('0') - 1)
