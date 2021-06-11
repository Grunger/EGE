n = 4**625 - 2**311 + 2 ** 571 - 48
s = ''
while n:
    s += str(n % 4)
    n //= 4
print(s.count('1'))
