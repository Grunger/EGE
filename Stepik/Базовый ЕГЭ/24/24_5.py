s = open('24_3.txt').read().strip()
mx = 0
k = 0
for i in range(len(s) - 2):
    if s[i:i + 3] != 'DIV':
        k += 1
    else:
        mx = max(mx, k + 2)
        k = 0
mx = max(mx, k)
print(mx)
s1 = s.split('DIV')
print(max(len(i) + 4 for i in s1))