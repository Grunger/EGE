from itertools import product

pairs = [''.join(i) for i in product('ABC', repeat=2)]
s = open('24.txt').read().strip()
mx = 0
for start in range(2):
    k = 0
    for i in range(start, len(s), 2):
        if s[i:i + 2] in pairs:
            k += 1
        else:
            mx = max(mx, k)
            k = 0
    mx = max(mx, k)
print(mx)
#
# # Через замены
s = s.replace('B', 'A').replace('C', 'A').replace('AA', '*')
k = 0
mx = 0
for i in range(len(s)):
    if s[i] == '*':
        k += 1
        mx = max(mx, k)
    else:
        k = 0
print(mx)

s = open('24.txt').read().strip()
s = s.replace('B', 'A').replace('C', 'A').replace('AA', '*')
for i in 'ABCQWERTYUIOPSDFGHJKLZXVNM':
    s = s.replace(i, ' ')
print(len(max(s.split(), key=len)))

f = open('24.txt').read().strip()
f = f.replace('B', 'A').replace('C', 'A')
i = 0
while 'A' * i in f:
    i += 1
print((i - 1) // 2)
