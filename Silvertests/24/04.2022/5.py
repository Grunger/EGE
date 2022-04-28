f = open('24-2.txt')
s = f.read().strip()
m = 0
k = 1
for i in range(len(s) - 2):
    if not (s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 1] == s[i + 2]):
        m = max(m, k)
        k = 1
    else:
        k += 1
print(m)

