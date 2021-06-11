s = open('24_1428_kab.txt').read().strip()
# s = open('test.txt').read().strip()
# ZZZZXYZZZXYZ
max_k = 0
k = 0
for i in range(len(s) - 1):
    if s[i:i + 2] == 'XY' or s[i:i + 2] == 'XZ':
        # print(s[i:i + 2])
        k = 0
    k += 1
    max_k = max(max_k, k)
print(max_k)
