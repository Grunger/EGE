f = open('24-2.txt')
s = f.read().strip()
m = 0
k = 1
for i in range(len(s) - 2):
    if s[i] == s[i + 2] and s[i] != s[i + 1]:
        m = max(m, k + 1)
        k = 1
    elif s[i + 1] == s[i + 2]:
        m = max(m, k + 1)
        k = 0
    elif s[i] == s[i + 1]:
        k = 1
    else:
        k += 1
    if k == m:
        print(s[i - k - 1:i + 10])
print(m)
