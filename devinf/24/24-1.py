mx = 0
k = 0
s = open('24_1.txt').read().strip()
for i in range(len(s)):
    if s[i:i + 2] in ('BD', 'DB'):
        mx = max(mx, k + 1)
        k = 0
    else:
        k += 1
mx = max(mx, k + 1)
print(mx)
for sub in ('BD', 'DB'):
    while sub in s:
        s = s.replace(sub, sub[0] + ' ' + sub[1])
print(len(max(s.split(), key=len)))
