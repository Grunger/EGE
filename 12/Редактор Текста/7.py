def record(s, pos, c):
    return ''.join([c if i == pos else s[i] for i in range(len(s))])


def delete(s, pos):
    return ''.join([s[w] for w in range(len(s)) if w != pos])


a = 'bbccaabaab'
q = 1
i = 0
while q < 3:
    c = a[i]
    if q == 1 and c == 'a':
        a = delete(a, i)
        i -= 1
    if q == 1 and c == 'b':
        a = record(a, i, 'c')
    if q == 1 and c == 'c':
        a = record(a, i, 'b')
    i += 1
    if i == len(a):
        q = 3
    print(a, i)
print(a)
