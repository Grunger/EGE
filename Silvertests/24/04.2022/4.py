f = open('24-1.txt')
s = f.read().strip()
m = 0
k = 1
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        m = max(m, k)
        k = 1
    else:
        k += 1
print(m)

