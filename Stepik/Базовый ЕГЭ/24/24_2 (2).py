s = open('24_1.txt').read().strip()
mx = 0
k = 0
for c in s:
    if c != 'E':
        k += 1
    else:
        mx = max(mx, k)
        k = 0
mx = max(mx, k)
print(mx)
