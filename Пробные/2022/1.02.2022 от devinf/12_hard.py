a = 'ДИСТАНТ'
i = len(a)
k = 2
b = 'А'
while i >= 0:
    c = a[i - 2]
    b = b + c
    i = i - k
b = b + 'ЕЛА'
print(b)