f = open('24-1.txt')
m = 0
k = 0
cnt = 0
s = f.read().strip()

for i in range(len(s) - 1):
    cnt += 1
    if s[i] == 'A'or s[i] == 'E':
        k += 1
    if s[i] + s[i + 1] == 'BD' or s[i] + s[i + 1] == 'DB':
        if k >= 50:
            m = max(m, cnt)
        k = 0
        cnt = 0
print(m)
