x = 7 * 512 ** 560 + 5 * 64 ** 740 - 3 * 8 ** 45 + 7 * 8 ** 54 - 31
s = oct(x)[2:]
k = 0
for i in range(len(s) - 1):
    if s[i] > s[i + 1]:
        k += 1
print(k)
