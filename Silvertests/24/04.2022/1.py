f = open('24-1.txt')
s = f.read().strip()
m = 0
k = 0
for i in range(1, len(s), 2):
    if s[i:i + 2] in {'ST', 'TS'}:
        k += 1
    else:
        m = max(m, k)
        k = 0
print(m)

