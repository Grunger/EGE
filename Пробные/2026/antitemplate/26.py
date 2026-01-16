f = open('t.txt')
n, d = map(int, f.readline().split())
s = [[], []]

for i in f:
    sz, t = map(int, i.split())
    s[t].append(sz)
s[0].sort()
s[1].sort()
mx = 0
for i in range(len(s[0])):
    a = [s[0][i]]
    i1 = 0
    i2 = 0
    while i1 < len(s[0]) or i2 < len(s[1]):
        while i2 < len(s[1]) and s[1][i2] < a[-1] + d:
            i2 += 1
        if i2 < len(s[1]):
            a.append(s[1][i2])
        while i1 < len(s[0]) and s[0][i1] < a[-1] + d:
            i1 += 1
        if i1 < len(s[0]):
            a.append(s[0][i1])
    if len(a) > mx:
        mx = len(a)
    else:
        break
for i in range(len(s[1])):
    a = [s[1][i]]
    i1 = 0
    i2 = 0
    while i1 < len(s[0]) or i2 < len(s[1]):
        while i1 < len(s[0]) and s[0][i1] < a[-1] + d:
            i1 += 1
        if i1 < len(s[0]):
            a.append(s[0][i1])
        while i2 < len(s[1]) and s[1][i2] < a[-1] + d:
            i2 += 1
        if i2 < len(s[1]):
            a.append(s[1][i2])
    if len(a) > mx:
        mx = len(a)
    else:
        break
print('Без увеличения d:', mx)
print(a)
# 76
mx2 = 0
while mx - mx2 != 1:
    d += 1
    print('Новое d', d)
    mx2 = 0
    for i in range(len(s[0])):
        a = [s[0][i]]
        i1 = 0
        i2 = 0
        while i1 < len(s[0]) or i2 < len(s[1]):
            while i2 < len(s[1]) and s[1][i2] < a[-1] + d:
                i2 += 1
            if i2 < len(s[1]):
                a.append(s[1][i2])
            while i1 < len(s[0]) and s[0][i1] < a[-1] + d:
                i1 += 1
            if i1 < len(s[0]):
                a.append(s[0][i1])
        if len(a) > mx2:
            mx2 = len(a)
            print(a)
        else:
            break
    for i in range(len(s[1])):
        a = [s[1][i]]
        i1 = 0
        i2 = 0
        while i1 < len(s[0]) or i2 < len(s[1]):
            while i1 < len(s[0]) and s[0][i1] < a[-1] + d:
                i1 += 1
            if i1 < len(s[0]):
                a.append(s[0][i1])
            while i2 < len(s[1]) and s[1][i2] < a[-1] + d:
                i2 += 1
            if i2 < len(s[1]):
                a.append(s[1][i2])
        if len(a) > mx2:
            mx2 = len(a)
            print(a)
        else:
            break
    print(mx2)
