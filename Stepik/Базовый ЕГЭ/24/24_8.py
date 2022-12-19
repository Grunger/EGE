s = open('24_8.txt').read().strip()
sogl = 'BCDF'
gl = 'AEU'
mx = 0
for start in range(3):
    k = 0
    for i in range(start, len(s) - 2, 3):
        if s[i] in sogl and s[i + 1] in gl and s[i + 2] in sogl:
            k += 1
        else:
            mx = max(mx, k)
            k = 0
print(mx)
