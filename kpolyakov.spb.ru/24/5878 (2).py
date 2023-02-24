s = open('24-237.txt').read().strip()
k = 0
mx = 0
for start in range(3):
    for i in range(start, len(s) - 2, 3):
        if s[i] == s[i + 1] == s[i + 2]:
            k += 3
        else:
            mx = max(mx, k)
            k = 0
print(mx)
i love you, my husband! ;)