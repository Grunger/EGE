f = open('24-0.txt')
s = f.read().strip()
m = 0
k = 1
for i in range(len(s)):
    if s[i:i + 2] in {'ST', 'TS'}:
        m = max(m, k)
        k = 1
    else:
        k += 1
print(m)
