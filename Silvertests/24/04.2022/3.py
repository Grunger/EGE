f = open('24-2.txt')
s = f.read().strip()
m = 0
k = 0
for i in range(len(s)):
    if s[i:i + 4] == 'TSTS':
        m = max(m, k + 3)
        k = 0
    else:
        k += 1
print(m)
s = s.split('TSTS')
print(max([len(i) for i in s]) + 6)
for i in s:
    print(len(i), i)