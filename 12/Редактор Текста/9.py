def record(s, pos, c):
    return ''.join([c if i == pos else s[i] for i in range(len(s))])


def delete(s, pos):
    return ''.join([s[w] for w in range(len(s)) if w != pos])


a = 'ababbababbaa'
q = 1
i = 0
while q < 4:
    c = a[i]
    if q == 2:
        if c == 'a':
            a = record(a, i, 'b')
        else:
            q = 1
    if q == 3:
        if c == 'b':
            a = record(a, i, 'a')
        else:
            q = 1
    if q == 1:
        a = delete(a, i)
        i -= 1
        if c == 'a':
            q = 3
        if c == 'b':
            q = 2
    i += 1
    if i == len(a):
        q = 4
    print(a, i)
print(a)

