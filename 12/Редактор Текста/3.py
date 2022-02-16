a = '5' * 10 + '7' * 10
i = len(a)
b = ''
while i > 0:
    c = a[i - 1]
    b += c
    i -= 3
print(b)
