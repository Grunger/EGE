s = open('24-4.txt').readline().strip()
print([s])
k = 1
t = s[0]
for i in range(1, len(s)):
    if s[i] < s[i - 1]:
        t += s[i]
        if len(t) > k:
            k = len(t)
    else:
        t = s[i]
print(k)
