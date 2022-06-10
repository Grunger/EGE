f = open('24-06.txt')
m = 0
s = f.read().strip()
s = s.split('R')

m = 0
for st in s:
    a = [0, 0, 0, 0]
    for i in range(len(st)):
        if st[i] == 'A':
            a.append(i)
            a.pop(0)
        m = max(m, i - a[0] + 1)
print(m)


for i in range(len(s)):
    s[i] = s[i].split('A')
for a in s:
    if len(a) <= 4:
        m = max(m, sum(len(i) for i in a) + len(a) - 1)
    else:
        for i in range(len(a) - 3):
            m = max(m, sum(len(i) for i in a[i:i + 4]) + len(a[i:i + 4]) - 1)
print(m)

