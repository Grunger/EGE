s = open('24.txt').read().strip()
m = 0
k = 1
for i in range(len(s) - 1):
    if s[i] >= s[i + 1]:
        k += 1
        m = max(k, m)
    else:
        m = max(k, m)
        k = 1
print(m)
