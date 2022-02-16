a = 'bbaaaabaaabbb'
q = 1
i = 0
while q < 4:
    c = a[i]
    if q == 2:
        if c == 'a':
            a = ''.join([a[w] for w in range(len(a)) if w != i])
            i -= 1
        else:
            q = 1
    if q == 3:
        if c == 'b':
            a = ''.join([a[w] for w in range(len(a)) if w != i])
            i -= 1
        else:
            q = 1
    if q == 1:
        if c == 'a':
            q = 2
        if c == 'b':
            q = 3
    i += 1
    if i == len(a):
        q = 4
print(a)
