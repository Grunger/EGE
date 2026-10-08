s = open('24_31230.txt').read().strip()
l = 0
r = 0
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
    l += 1
    r += 1
print(mn)
