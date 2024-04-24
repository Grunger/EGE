s = open('24_11_15.txt').read().strip()
s = s.split('W')
s = [len(i) for i in s]
m = 10 ** 10
d = 200
for i in range(len(s) - d - 1):
    k = sum(s[i:i + d + 1]) + d
    m = min(m, k)
print(m)
