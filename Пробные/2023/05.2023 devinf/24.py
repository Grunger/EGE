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

#s = s.replace('B', 'A').replace('C', 'A')
a = ['AA', 'AB', 'AC', 'BA' , 'BB', 'BC', 'CA', 'CB', 'CC']
for b in a:
    s = s.replace(b, '*')
k = 0
mx = 0
for i in range(len(s)):
    if s[i] == '*':
        k += 1
        mx = max(mx, k)
    else:
        k = 0
print(mx)
