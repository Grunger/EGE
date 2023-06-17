s = open('24.txt').read().strip()
mx = 0
k = 1
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        k += 1
    else:
        mx = max(mx, k)
        k = 1
mx = max(mx, k)
print(mx)

for c in 'QWERTYUIOPASDFGHJKLZXCVBNM':
    while c * 2 in s:
        s = s.replace(c + c, c + ' ' + c)
print(max(len(i) for i in s.split()))

