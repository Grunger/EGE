x = 3 * 15 ** 1140 + 2 * 15 ** 1025 + 15 ** 923 - 3 * 15 ** 85 + 2 * 15 ** 74 + 3
a = '0123456789AB'
s = ''
while x:
    s = str(a[x % 12]) + s
    x //= 15
print(s)
m = 0
for ch in a:
    k = 0
    for i in range(len(s)):
        if s[i] == ch:
            k += 1
        else:
            m = max(m, k)
            k = 0
print(m)
for i in range(len(s)):
    if s[i] == 'B':
        print(i)
