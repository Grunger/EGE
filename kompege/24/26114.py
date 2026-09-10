s = open('24_26114.txt').read().strip()
for c in '3579':
    s = s.replace(c, '1')
s = s.split('1')
mx = 0
for st in s:
    if st.count('Q') < 35:
        continue
    kq = 0
    i = 0
    while kq <= 35 and i < len(st):
        if st[i] == 'Q':
            kq += 1
        i += 1
    mx = max(mx, i + (kq == 35))
print(mx)

s = open('24_26114.txt').read().strip()
mx = 0
i = 0
kq = 0
k = 0
while i < len(s):
    if s[i] in '13579':
        kq = 0
        k = 0
    if s[i] == 'Q':
        kq += 1
    k += 1
    if kq == 35:
        mx = max(mx, k)
    i += 1
print(mx)


