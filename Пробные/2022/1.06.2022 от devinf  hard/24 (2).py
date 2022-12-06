f = open('24-06.txt')
m = 0
s = f.read().strip()
pr = []
for i in range(len(s)):
    if s[i] == 'R':
        pr.append(i)
# print(pr)
pa = []
for i in range(len(s)):
    if s[i] == 'A':
        pa.append(i)
# print(pa)
print(len(s))


m = 0
a = [0, pa[4] - 1]
cnt = 3
while a[-1] != pa[-1] - 1:
    k = 0
    for i in range(a[0], a[1] + 1):
        if i in pr:
            k += 1
    if k >= 2:
        m = max(m, a[1] - a[0] + 1)
    cnt += 1
    a[0] = a[1]
    a[1] = pa[cnt] - 1
a[0] = a[1]
a[1] = len(s)
k = 0
for i in range(a[0], a[1] + 1):
    if i in pr:
        k += 1
if k >= 2:
    m = max(m, a[1] - a[0] + 1)
print(m)
