f = open('24.txt').read().strip()
mx = 0
for start in range(2):
    k = 0
    for i in range(start, len(f), 2):
        if f[i:i + 2] in ('AB', 'CB'):
            k += 1
        else:
            mx = max(mx, k)
            k = 0
print(mx)
