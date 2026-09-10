s = open('24_31230.txt').read().strip()
s = s.split('ABC')
d = 110
mn = 10**10
for i in range(len(s) - d):
    t = 'ABC' + 'ABC'.join(s[i:i + d - 1]) + 'ABC'
    mn = min(mn, len(t))
print(mn)

s = open('24_31230.txt').read().strip()
l = 0
r = 0
d = 110
k = 0
while k < 110:
    if s[r:r + 3] == 'ABC':
        k += 1
    r += 1
while s[l:l + 3] != 'ABC':
    l += 1
mn = r - l + 3
r += 1
l += 1
while r < len(s):
    while r < len(s) and s[r:r + 3] != 'ABC':
        r += 1
    while s[l:l + 3] != 'ABC':
        l += 1
    mn = min(mn, r - l + 3)
    r += 1
    l += 1
print(mn)
