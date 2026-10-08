s = open('24.txt').read().strip()
m = 10 ** 10
n = len(s)
print(n)
for i in range(n):
    if i % 1000000 == 0:
        print(i)
    for j in range(i + 200, n):
        if s[i:j + 1].count('W') == 200:
            m = min(m, j - i + 1)
        if s[i:j + 1].count('W') > 200:
            break
print(m)