s = open('24.txt').read().strip()
lt = 0
rt = 0
k = 0
d = 200
m = 10**10
while rt < len(s):
    while rt < len(s) and k < d:
        if s[rt] == 'W':
            k += 1
        rt += 1
    while s[lt] != 'W':
        lt += 1
    m = min(m, rt - lt + 1)
    lt += 1
    k -= 1
if s[rt - 1] == 'W':
    m = min(m, rt - lt + 1)
print(m)
