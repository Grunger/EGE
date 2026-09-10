x = 9 ** 11 * 3 ** 20 - 3 ** 9 - 27
s = ''
k = 0
while x:
    if x % 3 == 2:
        k += 1
    x //= 3
print(k)
