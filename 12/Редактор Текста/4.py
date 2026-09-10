a = '5' * 20 + '7' * 20
i = 1
s = 1
b = ''
while i < len(a) - 1:
    if s == 1:
        c = a[i - 1]
        s = 0
    else:
        c = a[len(a) - i - 1]
        s = 1
    b += c
    i += 4
print(b)
