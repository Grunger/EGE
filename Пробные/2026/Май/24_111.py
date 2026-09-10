s = open('1_24.txt').read().strip()
print(s[-1])
alph = '0123456789abcdef'
print(alph[1::2])
mx = 0
for l in range(len(s)):
    if s[l] not in alph[1:]:
        continue
    r = l
    while s[r] in alph:
        r += 1
    r -= 1
    if s[r] not in alph[1::2]:
        while s[r] not in alph[1::2] and r > l:
            r -= 1
    mx = max(mx, r - l + 1)

print(mx)

