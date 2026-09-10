from time import time
s = open('24_31230.txt').read().strip()
print(len(s))
ts = time()
m = 1000
for i in range(len(s)):
    if i % 100_000 == 0:
        print(i, m, round(i / len(s) * 100, 1), time() - ts)
    for j in range(i, i + m):
        t = s[i:j + 1]
        if t.count('ABC') > 110:
            break
        if t.count('ABC') == 110:
            if t[-1] == 'C':
                m = min(m, len(t))
            break
print(m)

