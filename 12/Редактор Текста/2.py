a = 'ВИАНДОТ'
i = len(a)
b = 'М'
while i > 0:
    c = a[i - 2]
    b += c
    i -= 2
b += 'ОР'
print(b)
