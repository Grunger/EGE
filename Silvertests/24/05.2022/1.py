f = open('24-1.txt')
m = 0
k = 0
cnt = 0
s = f.read().strip()

for i in range(len(s) - 1):
    cnt += 1
    if s[i] == 'A':
        k += 1
    if s[i] + s[i + 1] == 'BC' or s[i] + s[i + 1] == 'CB':
        if k >= 2:
            m = max(m, cnt)
        k = 0
        cnt = 0
print(m)


m = 0
k = 0
s = s.replace('BC', 'X')
s = s.replace('CB', 'X')
for item in s.split('X'):
    if item.count('A') >= 2:
        m = max(m, len(item))
print(m)
