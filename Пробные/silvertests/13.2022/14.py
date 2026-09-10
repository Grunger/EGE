x = 15 * 15625 ** 25 - 625 ** 12 + 4 * 25 ** 54 - 8 * 5 ** 82 - 8

digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

answer = ''
while x:
    answer = answer + digits[x % 25]
    x //= 25
k = 0
for digit in answer:
    if digit.isalpha():
        k += 1
print(k)
