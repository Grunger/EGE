s = open('24_31230.txt').read().strip()
s = s.split('ABC')
d = 110
mn = 10**10
for i in range(len(s) - d):
    t = 'ABC'.join(s[i:i + d + 1])
    while t[:3] != 'ABC':
        t = t[1:]
    while t[-3:] != 'ABC':
        t = t[:-1]
    mn = min(mn, len(t))
print(mn)
