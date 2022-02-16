a = '101101'
i = 1
b = ''
while i <= len(a):
    c = a[i - 1]
    if c == '1':
        b += '0'
    if c == '0':
        b += '1'
    i += 1
print(b)
