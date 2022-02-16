def delete(s, pos):
    return ''.join([s[w] for w in range(len(s)) if w != pos])


a = '101101'
c = a[0]
if c == '1':
    q = 1
else:
    q = 2
a = delete(a, 0)
while q < 3:
    i = 1
    while i < len(a):
        i += 1
    if q == 1:
        a += '1'
    else:
        a += '0'
    q = 3
print(a)
