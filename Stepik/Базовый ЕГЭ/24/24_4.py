s = open('24_3.txt').read().strip()
mx = 0
k = 0
for i in range(len(s) - 1):
    if s[i:i + 2] not in ('VN', 'NV'):
        k += 1
    else:
        mx = max(mx, k + 1)
        k = 0
mx = max(mx, k)
print(mx)
