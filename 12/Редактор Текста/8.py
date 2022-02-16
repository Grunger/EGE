def record(s, pos, c):
    return ''.join([c if i == pos else s[i] for i in range(len(s))])


def delete(s, pos):
    return ''.join([s[w] for w in range(len(s)) if w != pos])


a = '10110011010'
q = 1
i = 0
while q < 3:
    c = a[i]
    if q == 1 and c == '0':
        a = record(a, i, '1')
    if q == 1 and c == '1':
        a = record(a, i, '0')
        q = 2
    if q == 2:
        a = delete(a, i)
        i -= 1
        q = 1
    i += 1
    if i == len(a):
        q = 3
    print(a, i)
print(a)
